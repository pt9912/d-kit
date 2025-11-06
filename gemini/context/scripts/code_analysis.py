#!/usr/bin/env python3
"""
Code Analysis Script
Performs static analysis on code files including syntax checking, linting, and security scanning.
"""

import sys
import os
import subprocess
import json
from pathlib import Path
from typing import List, Dict, Any

class CodeAnalyzer:
    """Performs various code quality checks"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.results = {
            "syntax_errors": [],
            "linting_issues": [],
            "security_issues": [],
            "summary": {}
        }
    
    def analyze_python(self, files: List[Path]) -> Dict[str, Any]:
        """Analyze Python files"""
        print("🐍 Analyzing Python files...")
        
        for file in files:
            # Syntax check
            try:
                with open(file, 'r') as f:
                    compile(f.read(), file, 'exec')
                print(f"  ✅ {file.name}: Syntax OK")
            except SyntaxError as e:
                error = f"{file}:{e.lineno}:{e.offset}: {e.msg}"
                self.results["syntax_errors"].append(error)
                print(f"  ❌ {file.name}: Syntax Error - {e.msg}")
            
            # Pylint
            self._run_pylint(file)
            
            # Bandit (security)
            self._run_bandit(file)
        
        return self.results
    
    def analyze_javascript(self, files: List[Path]) -> Dict[str, Any]:
        """Analyze JavaScript/TypeScript files"""
        print("📜 Analyzing JavaScript/TypeScript files...")
        
        for file in files:
            # ESLint
            self._run_eslint(file)
        
        return self.results
    
    def _run_pylint(self, file: Path):
        """Run pylint on Python file"""
        try:
            result = subprocess.run(
                ['pylint', str(file), '--output-format=json'],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.stdout:
                issues = json.loads(result.stdout)
                for issue in issues:
                    self.results["linting_issues"].append({
                        "file": str(file),
                        "line": issue.get("line"),
                        "message": issue.get("message"),
                        "type": issue.get("type")
                    })
                print(f"  ℹ️  {file.name}: {len(issues)} linting issues found")
            else:
                print(f"  ✅ {file.name}: No linting issues")
        except FileNotFoundError:
            print(f"  ⚠️  pylint not installed, skipping linting")
        except Exception as e:
            print(f"  ⚠️  Error running pylint: {e}")
    
    def _run_bandit(self, file: Path):
        """Run bandit security scanner"""
        try:
            result = subprocess.run(
                ['bandit', '-f', 'json', str(file)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.stdout:
                data = json.loads(result.stdout)
                issues = data.get("results", [])
                
                for issue in issues:
                    self.results["security_issues"].append({
                        "file": str(file),
                        "line": issue.get("line_number"),
                        "severity": issue.get("issue_severity"),
                        "confidence": issue.get("issue_confidence"),
                        "message": issue.get("issue_text")
                    })
                
                if issues:
                    print(f"  ⚠️  {file.name}: {len(issues)} security issues found")
                else:
                    print(f"  ✅ {file.name}: No security issues")
        except FileNotFoundError:
            print(f"  ℹ️  bandit not installed, skipping security scan")
        except Exception as e:
            print(f"  ⚠️  Error running bandit: {e}")
    
    def _run_eslint(self, file: Path):
        """Run ESLint on JavaScript/TypeScript file"""
        try:
            result = subprocess.run(
                ['eslint', '-f', 'json', str(file)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.stdout:
                data = json.loads(result.stdout)
                for file_result in data:
                    messages = file_result.get("messages", [])
                    for msg in messages:
                        self.results["linting_issues"].append({
                            "file": file_result["filePath"],
                            "line": msg.get("line"),
                            "message": msg.get("message"),
                            "severity": msg.get("severity")
                        })
                    
                    if messages:
                        print(f"  ℹ️  {file.name}: {len(messages)} issues found")
                    else:
                        print(f"  ✅ {file.name}: No issues")
        except FileNotFoundError:
            print(f"  ℹ️  eslint not installed, skipping")
        except Exception as e:
            print(f"  ⚠️  Error running eslint: {e}")
    
    def generate_report(self) -> str:
        """Generate summary report"""
        total_issues = (
            len(self.results["syntax_errors"]) +
            len(self.results["linting_issues"]) +
            len(self.results["security_issues"])
        )
        
        report = "\n" + "="*60 + "\n"
        report += "CODE ANALYSIS REPORT\n"
        report += "="*60 + "\n\n"
        
        report += f"Total Issues Found: {total_issues}\n"
        report += f"  - Syntax Errors: {len(self.results['syntax_errors'])}\n"
        report += f"  - Linting Issues: {len(self.results['linting_issues'])}\n"
        report += f"  - Security Issues: {len(self.results['security_issues'])}\n\n"
        
        if self.results["syntax_errors"]:
            report += "SYNTAX ERRORS:\n"
            for error in self.results["syntax_errors"]:
                report += f"  ❌ {error}\n"
            report += "\n"
        
        if self.results["security_issues"]:
            report += "SECURITY ISSUES:\n"
            for issue in self.results["security_issues"]:
                report += f"  ⚠️  {issue['file']}:{issue['line']} - {issue['message']}\n"
            report += "\n"
        
        if total_issues == 0:
            report += "✅ All checks passed!\n"
        else:
            report += f"❌ Found {total_issues} issues that should be addressed.\n"
        
        return report


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python code_analysis.py <project_path>")
        sys.exit(1)
    
    project_path = sys.argv[1]
    
    if not os.path.exists(project_path):
        print(f"Error: Path {project_path} does not exist")
        sys.exit(1)
    
    analyzer = CodeAnalyzer(project_path)
    project = Path(project_path)
    
    # Find all Python files
    py_files = list(project.rglob("*.py"))
    if py_files:
        analyzer.analyze_python(py_files)
    
    # Find all JS/TS files
    js_files = list(project.rglob("*.js")) + list(project.rglob("*.ts")) + list(project.rglob("*.tsx"))
    if js_files:
        analyzer.analyze_javascript(js_files)
    
    # Generate report
    report = analyzer.generate_report()
    print(report)
    
    # Save report
    report_file = project / "code_analysis_report.txt"
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"\n📄 Report saved to: {report_file}")
    
    # Exit with error code if issues found
    total_issues = (
        len(analyzer.results["syntax_errors"]) +
        len(analyzer.results["security_issues"])
    )
    sys.exit(1 if total_issues > 0 else 0)


if __name__ == "__main__":
    main()
