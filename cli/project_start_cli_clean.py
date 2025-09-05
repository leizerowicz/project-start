#!/usr/bin/env python3
"""
Project-Start Enhanced CLI - Interactive specification-driven development tool

Usage:
    python3 project_start_cli.py                     # Interactive menu
    python3 project_start_cli.py /enhance-step-1     # Step 1: Discovery
    python3 project_start_cli.py /enhance-step-2     # Step 2: SPARC Planning
    python3 project_start_cli.py /enhance-step-3     # Step 3: Context Systems
    python3 project_start_cli.py /enhance-step-4     # Step 4: PACT Framework
    python3 project_start_cli.py /project-start-enhanced  # Complete workflow
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

# ASCII Art Banner
BANNER = """
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ███████╗   ██║   ███████║██████╔╝   ██║
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚════██║   ██║   ██╔══██║██╔══██╗   ██║
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ███████║   ██║   ██║  ██║██║  ██║   ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
"""

TAGLINE = "Specification-Driven Development with AI Agent Collaboration"


class ProjectStartCLI:
    def __init__(self):
        self.project_root = self._detect_project_root()
        self.vscode_env = self._detect_vscode_environment()

    def _detect_vscode_environment(self) -> bool:
        """Detect if running in VS Code environment"""
        return (
            os.environ.get("VSCODE_PID") is not None
            or os.environ.get("TERM_PROGRAM") == "vscode"
            or "vscode" in os.environ.get("TERM_PROGRAM_VERSION", "").lower()
        )

    def _detect_project_root(self) -> Path:
        """Detect the project root directory"""
        current = Path.cwd()

        # Check for .project-start-config file
        config_file = current / ".project-start-config"
        if config_file.exists():
            try:
                with open(config_file, "r") as f:
                    for line in f:
                        if line.startswith("TARGET_PROJECT_ROOT="):
                            return Path(line.split("=", 1)[1].strip())
            except Exception:
                pass

        return current

    def show_banner(self):
        """Display the Project-Start banner"""
        print(BANNER)
        print(f"\n{'='*80}")
        print(f"{TAGLINE:^80}")
        print(f"{'='*80}")

    def ask_question(
        self, question: str, default: str = "", required: bool = True
    ) -> str:
        """Ask a question with optional default value"""
        prompt = f"\n{question}"
        if default:
            prompt += f" (default: {default})"
        prompt += ": "

        while True:
            answer = input(prompt).strip()
            if answer:
                return answer
            elif default:
                return default
            elif not required:
                return ""
            else:
                print("This field is required. Please enter a value.")

    def ask_multiple_choice(
        self, question: str, choices: list, default: str = ""
    ) -> str:
        """Ask a multiple choice question"""
        print(f"\n{question}")
        for i, choice in enumerate(choices, 1):
            marker = " (default)" if choice == default else ""
            print(f"{i}. {choice}{marker}")

        while True:
            try:
                answer = input("\nEnter your choice (number): ").strip()
                if not answer and default:
                    return default
                choice_num = int(answer)
                if 1 <= choice_num <= len(choices):
                    return choices[choice_num - 1]
                else:
                    print(f"Please enter a number between 1 and {len(choices)}")
            except ValueError:
                print("Please enter a valid number")

    def ask_yes_no(self, question: str, default: bool = True) -> bool:
        """Ask a yes/no question"""
        default_text = "Y/n" if default else "y/N"
        answer = input(f"{question} ({default_text}): ").strip().lower()
        if not answer:
            return default
        return answer in ["y", "yes", "true", "1"]

    def show_interactive_menu(self) -> None:
        """Show interactive menu for command selection"""
        self.show_banner()

        print("\n🚀 PROJECT-START ENHANCED CLI")
        print("=" * 50)
        print("Choose an action:")
        print()
        print("1. 📋 Step 1: Discovery & Specification Generation")
        print("2. 🎯 Step 2: SPARC Planning Methodology")
        print("3. 🧠 Step 3: Context Systems Creation")
        print("4. 🤝 Step 4: PACT Framework Deployment")
        print("5. ⚡ Complete Enhanced Workflow (All Steps)")
        print("6. ⚙️  Configure Project Root")
        print("7. ❓ Help & Documentation")
        print("8. 🚪 Exit")

        while True:
            try:
                choice = input("\nEnter your choice (1-8): ").strip()

                if choice == "1":
                    self._handle_step_1()
                    break
                elif choice == "2":
                    self._handle_step_2()
                    break
                elif choice == "3":
                    self._handle_step_3()
                    break
                elif choice == "4":
                    self._handle_step_4()
                    break
                elif choice == "5":
                    self._handle_complete_workflow()
                    break
                elif choice == "6":
                    self._handle_configure_project_root()
                    break
                elif choice == "7":
                    self._show_help_documentation()
                    break
                elif choice == "8":
                    print("\n👋 Goodbye!")
                    break
                else:
                    print("Please enter a number between 1 and 8")
            except KeyboardInterrupt:
                print("\n\n🛑 Operation cancelled by user")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

    def _handle_step_1(self) -> None:
        """Handle Step 1: Discovery & Specification Generation"""
        print("\n📋 STEP 1: DISCOVERY & SPECIFICATION GENERATION")
        print("=" * 55)

        description = self.ask_question(
            "Enter a brief project description", required=True
        )

        existing = self.ask_yes_no("Is this for an existing project?", default=False)

        self._run_step_command("/enhance-step-1", description, existing)

    def _handle_step_2(self) -> None:
        """Handle Step 2: SPARC Planning"""
        print("\n🎯 STEP 2: SPARC PLANNING METHODOLOGY")
        print("=" * 45)

        project_path = self.ask_question(
            "Enter project path (or press Enter for current directory)",
            default=str(self.project_root),
            required=False,
        )

        self._run_step_command("/enhance-step-2", project_path=project_path)

    def _handle_step_3(self) -> None:
        """Handle Step 3: Context Systems"""
        print("\n🧠 STEP 3: CONTEXT SYSTEMS CREATION")
        print("=" * 45)

        project_path = self.ask_question(
            "Enter project path (or press Enter for current directory)",
            default=str(self.project_root),
            required=False,
        )

        self._run_step_command("/enhance-step-3", project_path=project_path)

    def _handle_step_4(self) -> None:
        """Handle Step 4: PACT Framework"""
        print("\n🤝 STEP 4: PACT FRAMEWORK DEPLOYMENT")
        print("=" * 45)

        project_path = self.ask_question(
            "Enter project path (or press Enter for current directory)",
            default=str(self.project_root),
            required=False,
        )

        self._run_step_command("/enhance-step-4", project_path=project_path)

    def _handle_complete_workflow(self) -> None:
        """Handle Complete Enhanced Workflow"""
        print("\n⚡ COMPLETE ENHANCED WORKFLOW")
        print("=" * 40)

        description = self.ask_question(
            "Enter a brief project description", required=True
        )

        self._run_step_command("/project-start-enhanced", description)

    def _handle_configure_project_root(self) -> None:
        """Handle Configure Project Root"""
        print("\n⚙️  CONFIGURE PROJECT ROOT")
        print("=" * 35)

        self._run_step_command("/configure-project-root")

    def _show_help_documentation(self) -> None:
        """Show help and documentation"""
        print("\n❓ HELP & DOCUMENTATION")
        print("=" * 30)
        print()
        print("🔧 Available Commands:")
        print("  /enhance-step-1          - Discovery and specification generation")
        print("  /enhance-step-2          - SPARC planning methodology")
        print("  /enhance-step-3          - Context systems creation")
        print("  /enhance-step-4          - PACT framework deployment")
        print("  /project-start-enhanced  - Complete 4-step workflow")
        print("  /configure-project-root  - Configure project root")
        print()
        print("📚 Documentation:")
        print("  • README.md files in each step directory")
        print("  • Constitutional framework in PROJECT_START_CONSTITUTION.md")
        print("  • Memory systems in memory/ directory")
        print()
        print("🤖 AI Integration:")
        print("  • Supports Gemini CLI for intelligent document generation")
        print("  • Fallback templates when AI tools unavailable")
        print()
        input("\nPress Enter to return to main menu...")

    def _run_step_command(
        self,
        command: str,
        description: str = "",
        existing: bool = False,
        project_path: str = "",
    ):
        """Run a step command as a subprocess"""
        try:
            cmd = ["python3", "project_start_cli.py", command]

            if description:
                cmd.append(description)

            if existing:
                cmd.append("--existing-project")

            if project_path:
                cmd.extend(["--project-path", project_path])

            print(f"\n🚀 Running: {' '.join(cmd)}")
            print("=" * 50)

            # Run the command
            result = subprocess.run(cmd, cwd=self.project_root)

            if result.returncode == 0:
                print(f"\n✅ {command} completed successfully!")
            else:
                print(f"\n❌ {command} failed with return code {result.returncode}")

        except Exception as e:
            print(f"❌ Error running {command}: {e}")

    # Core step methods that call the respective enhancement scripts
    def enhance_step_1(
        self, description: str = "", existing_project: bool = False
    ) -> None:
        """Enhanced Step 1: Discovery and specification generation"""
        print("🔍 Starting Enhanced Step 1: Discovery & Specification Generation")
        print("=" * 70)

        try:
            cmd = ["./enhance-step-1"]
            if description:
                cmd.append(description)
            if existing_project:
                cmd.append("--existing-project")

            subprocess.run(cmd, cwd=self.project_root, check=True)
            print("✅ Step 1 completed successfully!")

        except subprocess.CalledProcessError as e:
            print(f"❌ Step 1 failed: {e}")
        except FileNotFoundError:
            print(
                "❌ enhance-step-1 script not found. Make sure you're in the correct directory."
            )

    def enhance_step_2(self, project_path: str = "") -> None:
        """Enhanced Step 2: SPARC Planning"""
        print("🎯 Starting Enhanced Step 2: SPARC Planning Methodology")
        print("=" * 60)

        try:
            cmd = ["./enhance-step-2"]
            if project_path:
                cmd.extend(["--project-path", project_path])

            subprocess.run(cmd, cwd=self.project_root, check=True)
            print("✅ Step 2 completed successfully!")

        except subprocess.CalledProcessError as e:
            print(f"❌ Step 2 failed: {e}")
        except FileNotFoundError:
            print(
                "❌ enhance-step-2 script not found. Make sure you're in the correct directory."
            )

    def enhance_step_3(self, project_path: str = "") -> None:
        """Enhanced Step 3: Context Systems"""
        print("🧠 Starting Enhanced Step 3: Context Systems Creation")
        print("=" * 55)

        try:
            cmd = ["./enhance-step-3"]
            if project_path:
                cmd.extend(["--project-path", project_path])

            subprocess.run(cmd, cwd=self.project_root, check=True)
            print("✅ Step 3 completed successfully!")

        except subprocess.CalledProcessError as e:
            print(f"❌ Step 3 failed: {e}")
        except FileNotFoundError:
            print(
                "❌ enhance-step-3 script not found. Make sure you're in the correct directory."
            )

    def enhance_step_4(self, project_path: str = "") -> None:
        """Enhanced Step 4: PACT Framework"""
        print("🤝 Starting Enhanced Step 4: PACT Framework Deployment")
        print("=" * 60)

        try:
            cmd = ["./enhance-step-4"]
            if project_path:
                cmd.extend(["--project-path", project_path])

            subprocess.run(cmd, cwd=self.project_root, check=True)
            print("✅ Step 4 completed successfully!")

        except subprocess.CalledProcessError as e:
            print(f"❌ Step 4 failed: {e}")
        except FileNotFoundError:
            print(
                "❌ enhance-step-4 script not found. Make sure you're in the correct directory."
            )

    def project_start_enhanced_workflow(self, description: str = "") -> None:
        """Complete enhanced workflow"""
        print("⚡ Starting Complete Enhanced Workflow")
        print("=" * 45)

        try:
            cmd = ["./project-start-enhanced"]
            if description:
                cmd.append(description)

            subprocess.run(cmd, cwd=self.project_root, check=True)
            print("✅ Complete workflow finished successfully!")

        except subprocess.CalledProcessError as e:
            print(f"❌ Complete workflow failed: {e}")
        except FileNotFoundError:
            print(
                "❌ project-start-enhanced script not found. Make sure you're in the correct directory."
            )

    def configure_project_root(self) -> None:
        """Configure project root"""
        print("⚙️ Configuring Project Root")
        print("=" * 30)

        try:
            subprocess.run(
                ["./scripts/configure-project-root.sh"],
                cwd=self.project_root,
                check=True,
            )
            print("✅ Project root configured successfully!")

        except subprocess.CalledProcessError as e:
            print(f"❌ Configuration failed: {e}")
        except FileNotFoundError:
            print("❌ configure-project-root.sh script not found.")


def main():
    parser = argparse.ArgumentParser(
        description="Project-Start Enhanced CLI - Specification-Driven Development"
    )
    parser.add_argument("command", nargs="?", help="Command to execute")
    parser.add_argument("description", nargs="?", help="Project description")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument(
        "--existing-project", action="store_true", help="Analyze existing project"
    )
    parser.add_argument("--project-path", help="Specify project path")

    # If no arguments provided, show interactive menu
    if len(sys.argv) == 1:
        cli = ProjectStartCLI()
        cli.show_interactive_menu()
        return

    args = parser.parse_args()
    cli = ProjectStartCLI()

    try:
        if args.command == "/enhance-step-1":
            cli.enhance_step_1(args.description or "", args.existing_project)
        elif args.command == "/enhance-step-2":
            cli.enhance_step_2(args.project_path or "")
        elif args.command == "/enhance-step-3":
            cli.enhance_step_3(args.project_path or "")
        elif args.command == "/enhance-step-4":
            cli.enhance_step_4(args.project_path or "")
        elif args.command == "/project-start-enhanced":
            cli.project_start_enhanced_workflow(args.description or "")
        elif args.command == "/configure-project-root":
            cli.configure_project_root()
        else:
            print(f"❌ Unknown command: {args.command}")
            print("\n🔧 Available commands:")
            print("• /enhance-step-1          - Discovery and specification generation")
            print("• /enhance-step-2          - SPARC planning methodology")
            print("• /enhance-step-3          - Context systems creation")
            print("• /enhance-step-4          - PACT framework deployment")
            print("• /project-start-enhanced  - Complete 4-step workflow")
            print("• /configure-project-root  - Configure project root")
            print("\n💡 Examples:")
            print('python3 project_start_cli.py /enhance-step-1 "Chat app"')
            print(
                "python3 project_start_cli.py /enhance-step-2 --project-path specs/001-my-project"
            )
            print("\n🚀 Or run without arguments for interactive menu:")
            print("python3 project_start_cli.py")

    except KeyboardInterrupt:
        print("\n\n🛑 Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if args.debug:
            import traceback

            traceback.print_exc()


if __name__ == "__main__":
    main()
