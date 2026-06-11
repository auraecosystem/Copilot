# Git Advanced Commands Cheat Sheet

Decision flow (pick the right tool)
- Shelve unfinished work -> `git stash`
- Copy commit(s) from another branch -> `git cherry-pick`
- Safely undo pushed/shared commit -> `git revert`
- Rewrite local (unshared) history -> `git reset` (or `git rebase -i`)

Quick reference
- git stash
  - Save: `git stash push -m "WIP: msg"`
  - Include untracked: `git stash push -u -m "WIP incl untracked"`
  - Apply: `git stash apply stash@{0}` (keeps stash) or `git stash pop` (apply + remove)
  - Branch from stash: `git stash branch feature/from-stash stash@{0}`

- git cherry-pick
  - Single commit: `git cherry-pick <sha>`
  - With trace: `git cherry-pick -x <sha>`
  - Range: `git cherry-pick A..B` (use carefully)
  - Do not commit immediately: `git cherry-pick -n <sha>`
  - Conflicts: fix → `git add <files>` → `git cherry-pick --continue`
  - Abort: `git cherry-pick --abort`

- git revert
  - Single commit: `git revert <sha>`
  - Revert range as one commit:
    `git revert --no-commit A..B ; git commit -m "Revert A..B"`
  - Revert merge: `git revert -m 1 <merge-sha>` (choose parent)
  - Conflicts: fix → `git add <files>` → `git revert --continue`
  - Abort: `git revert --abort`

- git reset
  - Move HEAD only (keep staged): `git reset --soft <commit>`
  - Move HEAD, unstage changes (keep work tree): `git reset <commit>`  # default = --mixed
  - Hard reset (discard changes): `git reset --hard <commit>`
  - Unstage file: `git reset HEAD path/to/file`
  - Recover: `git reflog` → `git checkout -b recover <sha>` or `git reset --hard <sha>`

Full example workflows
- Backport commit to release:
  ```
  git fetch origin
  git checkout release/v1.2
  git pull --ff-only origin release/v1.2
  git cherry-pick -x 4f7a1b2
  # resolve conflicts if needed: git add <files>; git cherry-pick --continue
  git push origin release/v1.2
  ```

- Safely undo pushed commit:
  ```
  git checkout main
  git pull origin main
  git revert 7d9f0a3
  # resolve conflicts if any: git add <files>; git revert --continue
  git push origin main
  ```

- Remove pushed commits (safe = revert, dangerous = reset+force)
  - Revert (safe):
    ```
    git checkout feature
    git pull origin feature
    git revert <sha-B>
    git revert <sha-A>
    git push origin feature
    ```
  - Reset + force (coordinate with team):
    ```
    git fetch origin
    git checkout feature
    git reset --hard GOOD_SHA
    git push --force-with-lease origin feature
    ```

Conflict resolution (generic)
1. `git status`
2. Edit files to resolve conflict markers (<<<<<<, >>>>>>)
3. `git add <resolved-files>`
4. `git <operation> --continue`   # e.g., cherry-pick/revert/rebase
5. Or `git <operation> --abort` to cancel

Safety tips
- Prefer `git revert` on shared branches.
- Use `--force-with-lease` instead of `--force`.
- Use `-x` when cherry-picking for traceability.
- Inspect with `git status`, `git log`, `git diff` before destructive ops.

`git reflog` is your friend for recovery after destructive changes.
``` ````

Commands you can run locally to add CHEATSHEET.md and finalize
- (clone or fetch the repo, then)
  git fetch origin
  git checkout tools/git-helper           # switch to the branch I created
  # create CHEATSHEET.md with the content above (or copy/paste)
  chmod +x git-helper.sh                  # ensure the helper is executable locally if needed
  git add CHEATSHEET.md git-helper.sh
  git commit -m "tools: add cheat sheet; ensure helper script executable"
  git push origin tools/git-helper

If you prefer I commit CHEATSHEET.md for you
- Reply: proceed
  - I will commit CHEATSHEET.md to tools/git-helper and push the branch (no changes to other branches).
  - After that I’ll post the branch URL and the exact commit hash for review and you can open a PR or merge.

If you prefer to keep control locally
- Reply: give me files and I’ll paste both final files and exact commands for you to run locally (already included above).

Optional next steps I can take after CHEATSHEET.md is added
- Add tailored examples for specific branches or commit SHAs (if you provide them).
- Create a Pull Request from tools/git-helper into your chosen target branch.
- Add CI check or a README snippet with script usage examples.

Which do you want me to do now? Reply with exactly one of:
- proceed  (I will commit CHEATSHEET.md to tools/git-helper)
- give me files  (I’ll paste final files and commands for you to run locally — already mostly provided)
- modify: <edit instructions>  (tell me what to change in the cheat sheet or script)
- add examples: <branch and SHAs>  (give branches/SHAs and I’ll add tailored examples)
