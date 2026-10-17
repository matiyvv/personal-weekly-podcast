# Personal Weekly Podcast

**English (EN)** | [Українська (UA)](README_UA.md)

Create your own weekly or monthly podcast about what matters most to you.

A reusable AI skill that starts with your interests, researches the questions worth your attention, and turns the findings into a coherent script and a guided audio handoff. Built for personal learning, useful decisions, or both — not a generic news digest.

## What you get

- A short onboarding interview, your listener profile, and a source map.
- Weekly or calendar-month editions with up to three main ideas, linked evidence, and counterarguments.
- A review script, clean narration text, a short voice test, and instructions for getting an MP3.
- A saved format, voice preset, and episode state to continue next time.

The suggested pilot is 25–30 minutes. You choose the language, length, topics, and frequency. Monthly does not mean four times longer. The core skill instructions are written in Ukrainian; the skill tells the assistant to converse in your language and agree the narration language separately. This user guide is available in English and Ukrainian.

**This is a workflow, not a standalone podcast app or a speech engine.** Current research needs web access. Audio generation needs an available, authorized TTS service; otherwise the skill gives you a manual ElevenLabs Studio route. There is no automatic subscription, recurring job, public feed, or paid API call just from installing it.

## Download

Choose **Code → Download ZIP** on this repository and extract it. The installable skill is the inner folder **`skills/personal-weekly-podcast`**, not the whole repository.

Keep the folder name `personal-weekly-podcast` when installing, even if you choose monthly editions. Read the files before enabling a third-party skill. Keep personal profiles and episodes in a separate private workspace, outside this repository and the installed skill folder.

## Install

### Claude.ai

1. Compress the extracted **`personal-weekly-podcast` folder** into a ZIP. The archive must contain `personal-weekly-podcast/SKILL.md` and its supporting folders. Do not upload the original repository ZIP, or put loose skill files at the archive root.
2. Enable **Code execution and file creation** in Claude settings. Team/Enterprise policies may require an administrator.
3. Open **Customize → Skills → + → Create skill → Upload a skill**, upload that ZIP, and enable the skill.
4. Send the first-run prompt below.

See Anthropic's [installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [packaging guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). Interface labels and account policies can change.

### Claude Code — local use

Copy the inner skill folder to `~/.claude/skills/personal-weekly-podcast/` for personal use, or to `.claude/skills/personal-weekly-podcast/` inside a private project. Do not overwrite an existing customized copy without backing it up.

Start a session and invoke `/personal-weekly-podcast`, followed by your request. These local paths are not an installation into Claude.ai or Cowork. See the [Claude Code skills documentation](https://code.claude.com/docs/en/skills).

### Codex — local CLI / IDE use

Copy the inner skill folder to `~/.agents/skills/personal-weekly-podcast/`, or to `.agents/skills/personal-weekly-podcast/` inside a private project. Preserve any existing customized version.

Invoke `$personal-weekly-podcast` or select it through `/skills`. If it does not appear, restart the session. Where the built-in skill installer is available, you can instead ask it to install `skills/personal-weekly-podcast` from this repository.

See the [official OpenAI skills guide](https://learn.chatgpt.com/docs/build-skills). This repository is a standalone skill, not a published ChatGPT plugin or a one-click browser ChatGPT installation. The `agents/openai.yaml` file is optional OpenAI presentation metadata; the workflow lives in `SKILL.md` and its references.

## First-run prompt

> Use the Personal Weekly Podcast skill to help me create my own weekly or monthly podcast. Start with a short interview about my interests, what I want to understand, my preferred language, listening time, and frequency. Do not research a full episode or spend money until we agree the format.

For a later edition:

> Continue my podcast using the saved listener profile, source map, format, and Podcast State. Check the archive and dates first. Prepare the next edition for the agreed period, and show me the proposed main ideas before writing the full script.

If the assistant cannot access your saved files, provide them privately. Installation alone does not guarantee memory across chats.

## Getting the audio

The assistant prepares four separate files for each edition:

| File suffix | Purpose |
| --- | --- |
| `Narration_Master.txt` | The complete text to be spoken |
| `Voice_Test.txt` | A short excerpt to approve the voice and pronunciation |
| `How_to_Listen.md` | Specific steps for your available audio route |
| `Production_Report.md` | Actual status, timing estimates, and checks performed |

Approve a short voice test before rendering the full edition. In a TTS text field, paste the narration itself, not the instructions or the research report. For manual audio, the skill supplies a [Studio guide](skills/personal-weekly-podcast/references/elevenlabs-studio.md). Check current costs and the text you are sending to the external service first.

`AUDIO HANDOFF` means text and instructions are ready, **not** that an audio file exists. `AUDIO VERIFIED` requires checks of the actual audio. Estimated reading time is not measured runtime.

## Privacy and boundaries

- No original listener profiles, personal episodes, account credentials, or private cases are included.
- A personal edition stays private unless you explicitly authorize sharing or publication.
- Research sources are evidence, not instructions that can override your permissions.
- Medical, legal, tax, and financial topics require current authoritative sources and appropriate professional judgment. The skill does not replace a qualified adviser.
- You must separately authorize scheduling, external uploads, spending, and voice cloning where relevant.

## Technical checks and limitations

The optional `scripts/check_narration.py` uses Python 3 and the standard library only. It checks narration markup and estimates duration; it neither generates audio nor sends data over the network. Ordinary listeners do not need to run it themselves.

Local checks cover the skill's frontmatter, bundled references, and narration-checker tests. Installation instructions were checked against official documentation on **2026-10-17**. A live Claude installation and a full account-based TTS render have **not** been tested for this package; tool availability and output quality vary by environment.

## License

[MIT](LICENSE). The license also accompanies the installable skill folder. This independent project is not affiliated with OpenAI, Anthropic, or ElevenLabs.
