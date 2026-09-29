---
name: three-lines
description: Compress any content into at most three dense lines chosen for the reader, by predicting the three questions the reader would ask first and answering one per line. Use when the user asks for a 3-line summary, "3줄 요약", "세 줄로", "tldr", or a short summary to share with a teammate, channel, PR, or issue — e.g. after fixing a bug. Not for general "summarize this" requests where a longer summary may be wanted.
---

# Three Lines

## Goal

Produce the three lines a specific reader most needs, not a shrunken copy of the source. What goes into the lines changes with the situation: a bug fix shared with a teammate needs different lines than meeting notes sent to someone who missed the meeting.

## Workflow

1. **Pick the target.**
   - If the user passed text, a file path, or a URL, summarize that. Read files and URLs first.
   - Otherwise, summarize the most recently completed unit of work in the current conversation.
   - Do not collect extra sources (git diff, logs) on your own. Anything the work touched is usually already in the conversation.
2. **Infer the reader.** Use what the user said ("팀원에게", "for the PM") and the nature of the content. Default to a teammate who lacks the conversation's context.
3. **Predict the reader's first three questions.** Ask: "Having received this summary, what would this reader want to know first?" Rank the questions by how much it hurts the reader not to know the answer. Examples:
   - Bug fix → teammate: What broke? / How was it fixed? / Does it affect me?
   - Meeting notes → absentee: What was decided? / Why? / What do I have to do?
   - Article → the user: Core claim? / Evidence? / Why it matters to me?
   These are illustrations, not a lookup table. Derive the questions from the actual reader and content every time.
4. **Answer one question per line**, following the rules below.
5. **Handle missing answers.** Never state a fact the source does not contain.
   - If an important question has no answer, say so explicitly — the gap is itself information: `원인 미확인 — 재현 조건(동시 요청 2건 이상)만 파악됨`.
   - If a minor question has no answer, replace it with the next-ranked question.
   - If the source holds fewer than three worthwhile facts, write only one or two lines. Never pad.
6. **Output** in the format below.

## Line Rules

- **One line answers one question.** Do not answer two questions in one line.
- **About 80 characters per line** (soft cap), so it reads without wrapping in Slack or a PR comment. If a line runs over, compress again before accepting it.
- **Concrete values first:** keep numbers, file and function names, error names, and dates. Drop vague words like "여러", "일부", "개선", "various", "improved".
- **Results, not process:** delete narration like "조사해보니", "확인 결과", "after investigating".
- **Joining clauses:** `—` or `→` may connect two facts that answer the same question.
- **Style:** terse report style by default. In Korean, end with noun-form endings (`~함`, `~됨`, `~음`). In English, drop the subject and start with a past-tense verb (`Fixed ...`). Write in the language of the conversation.
- If the user asks for a different style or language ("존댓말로", "in English"), apply it for that call only.
- **Three lines is a hard maximum.** Do not accept requests for more lines; that is a different task than a three-line summary.

## Output Format

Output only the lines, as a Markdown unordered list with one item per line:

```markdown
- 결제 API가 동시 요청 시 중복 청구됨 — 멱등키 검증이 트랜잭션 밖에 있었음.
- 검증을 트랜잭션 안으로 옮기고 멱등키에 unique 제약 추가해 해결.
- 기존 중복 건 12건 환불 처리 완료, 클라이언트 쪽 변경 없음.
```

- Render the list directly; do not wrap it in a code block.
- Output nothing else: no preamble, no divider, no notes on the chosen reader or questions, no alternative versions.
- If the user corrects the pick ("독자는 PM", "대상은 로그인 버그") or asks for another angle ("다른 관점으로"), redo the summary accordingly.
