from pathlib import Path
import json
import os
import shutil
import subprocess
import zipfile

project = Path(__file__).resolve().parents[1]
test_file = project / 'tests' / 'counter.spec.js'
original = test_file.read_text()
examples = project / 'examples'
examples.mkdir(exist_ok=True)
environment = {**os.environ, 'FORCE_COLOR': '0'}
environment.pop('NO_COLOR', None)


def run_test(log_name):
    result = subprocess.run(
        ['./run.sh', 'test'], cwd=project, env=environment,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    (examples / log_name).write_text(result.stdout)
    print(result.stdout, flush=True)
    return result


first = run_test('initial-pass.txt')
if first.returncode != 0:
    raise SystemExit('Первый запуск завершился ошибкой; исходный тест сохранён.')

wrong = original.replace("await expect(quantity).toHaveText('1');",
                         "await expect(quantity).toHaveText('2');")
assert wrong != original
try:
    test_file.write_text(wrong)
    failure = run_test('expected-failure.txt')
    if failure.returncode != 1:
        raise RuntimeError('Учебный ошибочный тест должен завершиться с кодом 1.')
    if 'Expected' not in failure.stdout or 'Received' not in failure.stdout:
        raise RuntimeError('В выводе нет сравнения ожидаемого и фактического значений.')
    failure_report = examples / 'failure-report'
    shutil.copytree(project / 'playwright-report', failure_report, dirs_exist_ok=True)
    traces = list(failure_report.rglob('*.zip'))
    screenshots = list(failure_report.rglob('*.png'))
    if not traces or not screenshots:
        raise RuntimeError('Отчёт не содержит снимок экрана или трассу.')
    for trace in traces:
        with zipfile.ZipFile(trace) as archive:
            if not any(name.endswith('.trace') for name in archive.namelist()):
                raise RuntimeError('В архиве нет данных трассы.')
finally:
    test_file.write_text(original)

restored = run_test('restored-pass.txt')
if restored.returncode != 0:
    raise SystemExit('Итоговый запуск завершился ошибкой.')
assert test_file.read_text() == original

package = json.loads((project / 'node_modules/@playwright/test/package.json').read_text())
summary = {
    'playwright_version': package['version'],
    'initial_test': 'passed',
    'demonstration_with_expected_2': 'failed as expected; received 1',
    'failure_screenshot_saved': bool(screenshots),
    'failure_trace_saved': bool(traces),
    'final_test': '1 passed',
    'source_restored': True,
}
(examples / 'verification.json').write_text(
    json.dumps(summary, ensure_ascii=False, indent=2) + '\n'
)
print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
