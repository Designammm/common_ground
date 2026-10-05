# Protocol

## Draft Message Flow

```
HUMAN
  ↓
INTENT
  ↓
CONTEXT
  ↓
INTERPRETATION
  ↓
COMMON REPRESENTATION
  ↓
MACHINE ACTION
  ↓
RESULT
  ↓
FEEDBACK
  ↓
HUMAN
```

## Design Questions

- What information must every message carry?
- Which parts can remain ambiguous?
- How should uncertainty be represented?
- How does a machine expose its interpretation?
- How does a human correct the interpretation?
- When does interpretation become action?
- How is feedback stored?

These questions define the protocol before implementation.
