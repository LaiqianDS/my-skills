---
name: cold-email
description: Generate high-conversion cold emails, cold DMs, and outreach messages. Use this skill whenever the user wants to write a cold email, cold DM, outreach message, pitch email, networking email, follow-up email, or reach out to someone they don't know. Also trigger when the user says things like "email this person", "reach out to [name]", "write a pitch to", "draft an outreach", "follow up with", "cold message", "introduction email to someone I don't know", or asks for help contacting investors, potential clients, hiring managers, professors, or anyone they lack a warm intro to. Do NOT use for marketing blasts, newsletters, internal team emails, or messages to people the user already has a relationship with.
---

# Cold Email Skill

Generate cold emails and DMs that get replies. Based on a proven framework with 40%+ reply rates.

## Core Philosophy

Cold email works because most people never ask. They assume the answer is no, assume there's a process, assume someone like them doesn't get to ask. The worst outcome is being ignored, and you're already at zero.

The goal is not to write a "good email." The goal is to make it so easy for the recipient to say yes that saying no feels like more work.

## Before Writing: Information Gathering

Before drafting anything, you need these inputs from the user. Ask for whatever is missing:

1. **Who is the recipient?** Name, role, company, and anything specific about them (a recent post, talk, product launch, article, decision, achievement). The more specific, the better the email.
2. **What does the user want?** The actual ask. Not "connect" or "network." The concrete outcome: a meeting, a demo, a referral, funding, a job interview, a partnership, information, a favor.
3. **Why should the recipient care?** What's in it for them? If the user can't articulate this, help them figure it out. If there's genuinely nothing in it for the recipient, the email should at minimum be respectful of their time and make the ask extremely low-friction.
4. **What platform?** Email, Twitter/X DM, LinkedIn, Instagram DM. This changes tone and length.
5. **Any context on the user?** What makes them credible or interesting in this context? Not their life story, just the one thing that earns attention.

If the user provides a URL, profile, or other info about the recipient, use it to extract personalization hooks.

### When the user provides a URL or profile
If the user shares a LinkedIn profile, personal website, Twitter/X profile, blog post, or any URL related to the recipient, use web search and web fetch tools to pull specific details: recent posts, projects, talks, product launches, stated opinions, achievements. Extract 2-3 concrete personalization hooks. The best hook is always the most recent and specific thing the recipient did or said publicly. Never use generic observations like "I see you work in tech."

## The Five-Line Structure

Every cold email follows this skeleton. Five lines. Not five paragraphs.

```
Subject: [Specific thing they posted/did/said]

Hey [First name],

[Line 1: HOOK — One sentence proving you paid attention. Their post, talk, product, words. Specific.]

[Line 2: WHY THEM — One sentence on why you're reaching out, framed around THEM. Not you.]

[Line 3: YOUR OFFER — One sentence on what you're offering, focused on outcome for them.]

[Line 4: LOW-FRICTION CTA — Make it too easy to say yes.]

- [Your first name]
```

If you can't say it in five lines, you don't understand the offer well enough. Compress.

## Rules That Matter

### Subject Line
The subject line determines whether the email gets opened. Everything else is irrelevant if this fails.

- Make it specific enough that only one person could have received it
- Reference something real about the recipient
- Never use: "Quick question", "Following up", "Partnership Opportunity", "Intro", or anything that reads like a template

Good examples:
- "your talk at [event] on [topic]"
- "[their product] + [your product] idea"
- "re: your [specific post/tweet] on [topic]"

### Opening Line
You have one line to prove this isn't a mass email. Use it.

- Reference something specific: their recent post, a product feature, a talk, a decision they made, an article they wrote
- Never open with: "Hope you're doing well", "I hope this finds you well", "My name is...", "I'm reaching out because..."

Strong openers:
- "I'll keep this short bc you don't care yet."
- "Saw your post on [x], had to reach out."
- "Built something that might 10x what you're working on."

### The Ask (CTA)
The ask must be so low-effort that saying yes is easier than deciding not to reply.

Never say: "would love to connect", "let me know if there's anything you need", "would be great to chat sometime"

Instead say:
- "Mind if I send a 2-min demo?"
- "Got 5 min for a quick yes/no?"
- "Can I send over a one-pager?"
- "Worth a quick look, or should I close this out?"

### Framing: Them, Not You
No one cares what you built. They care what it does for them.

- Wrong: "I built an AI tool that uses transformer architecture to..."
- Right: "This might save your team 5 hours a week on [specific task]."

Every sentence should pass the "so what?" test from the recipient's perspective.

### Tone
Write like a smart friend, not a desperate applicant. This is a vibe check, not a thesis.

- Use contractions
- Use fragments when they hit harder
- Sign with just your first name
- No corporate speak, no jargon walls, no "I would be honored"
- Confident but not arrogant. Direct but not pushy.

## Platform-Specific Adjustments

### Twitter/X DMs
- Shorter than email. 2-3 sentences max.
- Very casual. No subject line.
- Often just: hook + ask.
- Can reference their tweet directly.

### LinkedIn Messages
- Slightly more professional than Twitter, but still direct.
- No subject line filler.
- Avoid LinkedIn-speak ("synergy", "leverage", "thought leader").

### Cold Emails (standard)
- The full five-line structure.
- Include a subject line.
- Can be slightly longer if the context demands it, but default to short.

### Investor Emails
- Lead with traction. Numbers first, story second.
- If you have metrics, open with them: "We hit [X users] and [$Y MRR] in [Z months]."
- The ask is specific: "Raising [amount] for [purpose]. Would love 20 min to walk through the deck."
- Attach nothing unsolicited. Offer to send.

## Follow-Up Sequences

Most replies come from follow-ups, not the first email. No reply does not mean no. People are busy.

Generate follow-ups when the user asks, using this cadence:

**Follow-up 1 (Day 3):**
Short bump. "Bumping this up in case it got buried, no pressure either way."

**Follow-up 2 (Day 7):**
Give them an easy out. "Worth a quick look or should I close this out?" Giving an easy exit paradoxically increases reply rates.

**Follow-up 3 (Day 14+, only if there's new information):**
The best follow-up isn't a nudge, it's news. New traction, a new feature, a new data point, a relevant event. "Following up from last week. We just hit [milestone]. Would love to revisit."

Never follow up more than 3 times without new information. After that, move on.

## Output Format

When generating a cold email, always output:

1. **The email itself** (subject + body), clearly formatted and ready to copy
2. **A brief note on why specific choices were made** (2-3 sentences max, only if it helps the user iterate)

When generating follow-ups, output the full sequence with suggested timing.

If the user asks for multiple variants, produce 2-3 with different angles (different hooks, different framings of value, different CTAs) and briefly note what each variant optimizes for.

## Common Scenarios and How to Handle Them

**User wants a job but isn't "qualified":**
Focus the email on what they've done (projects, results) rather than credentials. Make the ask about a conversation, not an application.

**User wants to ask for money (scholarship, raise, funding):**
Be direct about the ask. State the specific amount. Frame it around why it makes sense for them to say yes, not why you need it.

**User wants to reach a famous/busy person:**
Shorter is better. The more important someone is, the less time they have. One specific compliment, one clear ask, done.

**User has no obvious value to offer:**
Lead with genuine curiosity or a specific insight about their work. The "value" can be as simple as being interesting, thoughtful, or having a relevant perspective. Not every cold email needs to offer ROI.

**User wants to cold email at scale (100+ emails):**
Advise them to create a template with clear personalization slots, not a fully generic blast. The personalization line (Line 1) must be unique per recipient. Everything else can be templated.
