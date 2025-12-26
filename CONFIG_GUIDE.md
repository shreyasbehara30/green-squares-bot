# Example: How to add more repositories to config.json

To add multiple repositories to the bot:

1. Open `config.json`
2. Add repository names in the format: "username/repo-name"
3. The bot will randomly select ONE repo per run

## Example configuration with multiple repos:

```json
{
  "repositories": [
    "shreyasbehara30/green-squares-bot",
    "shreyasbehara30/my-project",
    "shreyasbehara30/learning-notes",
    "shreyasbehara30/portfolio"
  ],
  "github_username": "shreyasbehara30",
  ...
}
```

## Safety Features Built-In:

✅ Only ONE repository is selected per run
✅ Max 1 commit per repository per day
✅ Automatic skip if README already updated today
✅ Repository ownership verification
✅ Random delay (5-40 minutes) before commit
✅ Meaningful, non-repetitive README updates

## Important Notes:

- Each repo must have a README.md file
- Bot only commits to repos owned by the configured user
- Never commits to forked repos or other users' repos
- All changes are transparent and documented
