#!/usr/bin/env python3
"""
Test Runner Script
Runs tests with coverage reporting for Python and JavaScript projects.
"""

import sys
import os
import subprocess
from pathlib import Path
from typing import Dict, Any

class TestRunner:
    """Runs tests and generates coverage reports"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.results = {
            "tests_run": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "coverage": 0.0
        }
    
    def run_python_tests(self) -> Dict[str, Any]:
        """Run pytest with coverage"""
        print("🐍 Running Python tests...")
        
        try:
            # Run pytest with coverage
            result = subprocess.run(
                [
                    'pytest',
                    '--cov=' + str(self.project_path),
                    '--cov-report=term-missing',
                    '--cov-report=html',
                    '--verbose',
                    str(self.project_path)
                ],
                capture_output=True,
                text=True,
                cwd=self.project_path
            )
            
            print(result.stdout)
            
            if result.returncode == 0:
                print("✅ All Python tests passed!")
                self._parse_pytest_output(result.stdout)
            else:
                print("❌ Some Python tests failed")
                self._parse_pytest_output(result.stdout)
            
            return self.results
            
        except FileNotFoundError:
            print("⚠️  pytest not installed. Install with: pip install pytest pytest-cov")
            return self.results
        except Exception as e:
            print(f"❌ Error running tests: {e}")
            return self.results
    
    def run_javascript_tests(self) -> Dict[str, Any]:
        """Run Jest tests"""
        print("📜 Running JavaScript tests...")
        
        # Check if package.json exists
        package_json = self.project_path / "package.json"
        if not package_json.exists():
            print("ℹ️  No package.json found, skipping JavaScript tests")
            return self.results
        
        try:
            # Run Jest
            result = subprocess.run(
                ['npm', 'test', '--', '--coverage'],
                capture_output=True,
                text=True,
                cwd=self.project_path
            )
            
            print(result.stdout)
            
            if result.returncode == 0:
                print("✅ All JavaScript tests passed!")
            else:
                print("❌ Some JavaScript tests failed")
            
            return self.results
            
        except FileNotFoundError:
            print("⚠️  npm not found")
            return self.results
        except Exception as e:
            print(f"❌ Error running tests: {e}")
            return self.results
    
    def _parse_pytest_output(self, output: str):
        """Parse pytest output to extract statistics"""
        lines = output.split('\n')
        
        for line in lines:
            # Parse test results line (e.g., "5 passed, 2 failed in 1.23s")
            if 'passed' in line or 'failed' in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if part == 'passed':
                        self.results["tests_passed"] = int(parts[i-1])
                    elif part == 'failed':
                        self.results["tests_failed"] = int(parts[i-1])
            
            # Parse coverage percentage
            if 'TOTAL' in line and '%' in line:
                parts = line.split()
                for part in parts:
                    if '%' in part:
                        try:
                            self.results["coverage"] = float(part.rstrip('%'))
                        except ValueError:
                            pass
        
        self.results["tests_run"] = (
            self.results["tests_passed"] + 
            self.results["tests_failed"]
        )
    
    def generate_report(self) -> str:
        """Generate test summary report"""
        report = "\n" + "="*60 + "\n"
        report += "TEST REPORT\n"
        report += "="*60 + "\n\n"
        
        report += f"Tests Run: {self.results['tests_run']}\n"
        report += f"Tests Passed: {self.results['tests_passed']} ✅\n"
        report += f"Tests Failed: {self.results['tests_failed']} ❌\n"
        report += f"Code Coverage: {self.results['coverage']:.1f}%\n\n"
        
        # Coverage assessment
        coverage = self.results["coverage"]
        if coverage >= 80:
            report += "✅ Coverage target met (≥80%)\n"
        elif coverage >= 60:
            report += "⚠️  Coverage below target (60-80%)\n"
        else:
            report += "❌ Coverage critically low (<60%)\n"
        
        # Overall status
        if self.results["tests_failed"] == 0 and coverage >= 80:
            report += "\n✅ All checks passed! Ready for deployment.\n"
        elif self.results["tests_failed"] == 0:
            report += "\n⚠️  All tests passed but coverage is low.\n"
        else:
            report += "\n❌ Tests failed. Fix issues before proceeding.\n"
        
        return report


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python run_tests.py <project_path>")
        sys.exit(1)
    
    project_path = sys.argv[1]
    
    if not os.path.exists(project_path):
        print(f"Error: Path {project_path} does not exist")
        sys.exit(1)
    
    runner = TestRunner(project_path)
    
    # Detect project type and run appropriate tests
    if (Path(project_path) / "pytest.ini").exists() or \
       list(Path(project_path).rglob("test_*.py")):
        runner.run_python_tests()
    
    if (Path(project_path) / "package.json").exists():
        runner.run_javascript_tests()
    
    # Generate report
    report = runner.generate_report()
    print(report)
    
    # Save report
    report_file = Path(project_path) / "test_report.txt"
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"\n📄 Report saved to: {report_file}")
    
    # Exit with error if tests failed
    sys.exit(1 if runner.results["tests_failed"] > 0 else 0)


if __name__ == "__main__":
    main()
