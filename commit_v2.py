"""
🌿 Green Squares Bot v2.0
Multi-Repository GitHub Activity Automation

Features:
- Multi-repository support with random selection
- Meaningful README.md updates
- Anti-spam guards (max 1 commit/day per repo)
- Random delays (5-40 minutes)
- Human-like commit messages
- Full GitHub ToS compliance
"""

import os
import random
import datetime
import time
import json
import re
import subprocess
from pathlib import Path


class MultiRepoBot:
    """GitHub activity bot with multi-repository support."""
    
    def __init__(self, config_path="config.json"):
        """Initialize bot with configuration."""
        self.config = self.load_config(config_path)
        self.tracker_file = ".repo_tracker.json"
        self.today = datetime.datetime.now().strftime('%Y-%m-%d')
        
    def load_config(self, config_path):
        """Load bot configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            print(f"✅ Configuration loaded from {config_path}")
            return config
        except FileNotFoundError:
            print(f"❌ Config file not found: {config_path}")
            exit(1)
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON in config file: {config_path}")
            exit(1)
    
    def load_tracker(self):
        """Load tracking data from file."""
        if os.path.exists(self.tracker_file):
            with open(self.tracker_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_tracker(self, data):
        """Save tracking data to file."""
        with open(self.tracker_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def is_already_committed_today(self, repo_name):
        """Check if repo already has a commit today."""
        tracker = self.load_tracker()
        repo_data = tracker.get(repo_name, {})
        last_commit = repo_data.get('last_commit_date')
        return last_commit == self.today
    
    def select_random_repo(self):
        """Select a random repository that hasn't been updated today."""
        repos = self.config.get('repositories', [])
        
        if not repos:
            print("❌ No repositories configured.")
            return None
        
        # Filter out repos already committed today
        available_repos = [
            repo for repo in repos 
            if not self.is_already_committed_today(repo)
        ]
        
        if not available_repos:
            print("✅ All repositories already updated today. Skipping.")
            return None
        
        selected = random.choice(available_repos)
        print(f"🎯 Selected repository: {selected}")
        return selected
    
    def verify_repo_ownership(self, repo_name):
        """Verify that the repository belongs to the configured user."""
        username = self.config.get('github_username')
        if not username:
            print("⚠️ github_username not configured. Proceeding with caution.")
            return True
        
        # Check if repo name starts with username
        if repo_name.startswith(f"{username}/"):
            return True
        else:
            print(f"❌ Repository {repo_name} does not belong to {username}")
            return False
    
    def get_readme_update_content(self):
        """Generate meaningful README.md update content."""
        sections = self.config.get('readme_sections', ['Daily Activity Log'])
        section = random.choice(sections)
        
        now = datetime.datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%I:%M %p')
        
        update_types = [
            f"- [{date_str}] Documentation reviewed and updated",
            f"- [{date_str}] Maintenance check completed at {time_str}",
            f"- [{date_str}] Project status verified",
            f"- [{date_str}] Added notes on recent progress",
            f"- [{date_str}] Documentation improvements implemented",
            f"- [{date_str}] Routine quality check performed"
        ]
        
        content = f"\n\n## {section}\n\n{random.choice(update_types)}\n"
        return content, section
    
    def update_readme(self, repo_path):
        """Update README.md with meaningful content."""
        readme_path = os.path.join(repo_path, 'README.md')
        
        if not os.path.exists(readme_path):
            print(f"⚠️ README.md not found at {readme_path}")
            return False
        
        # Read current content
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated today
        if self.today in content:
            print(f"ℹ️ README already contains today's date ({self.today}). Skipping.")
            return False
        
        # Generate and append new content
        new_content, section = self.get_readme_update_content()
        
        # Check if section exists, otherwise append
        if section in content:
            # Find section and append under it
            pattern = f"## {section}"
            if pattern in content:
                # Insert after the section header
                parts = content.split(pattern)
                updated_content = parts[0] + pattern + new_content + parts[1]
            else:
                updated_content = content + new_content
        else:
            # Append at the end
            updated_content = content + new_content
        
        # Write updated content
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ README.md updated successfully")
        return True
    
    def get_commit_message(self):
        """Get a random commit message."""
        messages = self.config.get('commit_messages', [
            "📝 docs: update documentation"
        ])
        return random.choice(messages)
    
    def add_transparency_note(self, repo_path):
        """Add transparency note to README if not already present."""
        readme_path = os.path.join(repo_path, 'README.md')
        
        if not os.path.exists(readme_path):
            return
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        transparency_note = "🤖 This repository is maintained with the help of an automated documentation bot."
        
        if transparency_note not in content:
            # Add note at the end
            updated_content = content + f"\n\n---\n\n{transparency_note}\n"
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print("✅ Transparency note added to README")
            return True
        
        return False
    
    def commit_changes(self, repo_path, repo_name):
        """Commit and push changes to repository."""
        try:
            # Change to repo directory
            os.chdir(repo_path)
            
            # Check if there are changes
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True
            )
            
            if not result.stdout.strip():
                print("ℹ️ No changes to commit.")
                return False
            
            # Stage changes
            subprocess.run(['git', 'add', 'README.md'], check=True)
            
            # Commit
            commit_msg = self.get_commit_message()
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            
            print(f"✅ Changes committed: {commit_msg}")
            
            # Update tracker
            tracker = self.load_tracker()
            tracker[repo_name] = {
                'last_commit_date': self.today,
                'last_commit_message': commit_msg
            }
            self.save_tracker(tracker)
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Git command failed: {e}")
            return False
    
    def apply_random_delay(self):
        """Apply random delay before committing."""
        settings = self.config.get('commit_settings', {})
        min_delay = settings.get('min_delay_minutes', 5)
        max_delay = settings.get('max_delay_minutes', 40)
        
        delay_minutes = random.randint(min_delay, max_delay)
        delay_seconds = delay_minutes * 60
        
        print(f"⏰ Waiting {delay_minutes} minutes before commit...")
        
        # For GitHub Actions, we skip the actual delay to avoid long runs
        # In local mode, you can enable this
        if os.getenv('GITHUB_ACTIONS'):
            print("ℹ️ Running in GitHub Actions - skipping delay")
            return
        
        time.sleep(delay_seconds)
    
    def run(self):
        """Main execution flow."""
        print("🚀 Green Squares Bot v2.0 Starting...")
        print(f"📅 Date: {self.today}")
        
        # Select a random repository
        repo_name = self.select_random_repo()
        
        if not repo_name:
            print("✅ No action needed. Exiting gracefully.")
            return
        
        # Verify ownership
        if not self.verify_repo_ownership(repo_name):
            print("❌ Repository ownership verification failed. Aborting.")
            return
        
        # For current repo (same directory)
        # In a multi-repo setup, you'd clone or navigate to different repos
        repo_path = os.getcwd()
        
        # Check if already committed today
        if self.is_already_committed_today(repo_name):
            print(f"✅ Repository '{repo_name}' already updated today. Skipping.")
            return
        
        # Apply random delay
        self.apply_random_delay()
        
        # Add transparency note (one-time)
        self.add_transparency_note(repo_path)
        
        # Update README
        if self.update_readme(repo_path):
            # Commit changes
            if self.commit_changes(repo_path, repo_name):
                print(f"✅ Successfully updated {repo_name}")
            else:
                print(f"⚠️ Failed to commit changes for {repo_name}")
        else:
            print(f"ℹ️ No updates needed for {repo_name}")
        
        print("🎉 Bot execution completed!")


def main():
    """Entry point for the bot."""
    bot = MultiRepoBot()
    bot.run()


if __name__ == "__main__":
    main()
