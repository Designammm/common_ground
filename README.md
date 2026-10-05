# COMMON GROUND

A working framework for a shared language between humans and machines.

## Status

**v0.1 — conceptual prototype**

Common Ground explores the layer between human intention and machine execution: a structured space where ambiguous human ideas can become interpretable machine instructions without reducing the human side to rigid commands.

## Core Model

Human Intent
→ Interpretation
→ Common Ground
→ Structured Representation
→ Machine Action
→ Feedback
→ Human Revision

The project is intentionally rough at this stage. The first objective is to establish the vocabulary, protocol, and pipeline before building a full implementation.

## Repository Structure

```
common_ground/
├── MANIFESTO.md
├── README.md
├── docs/
│   ├── CONCEPT.md
│   └── PROTOCOL.md
├── pipeline/
│   ├── input.py
│   ├── normalize.py
│   ├── interpret.py
│   ├── map.py
│   └── output.py
├── schemas/
│   └── message.schema.json
└── examples/
    ├── human-to-machine.json
    └── machine-to-human.json
```

## Principle

Common Ground is not intended to make humans communicate like machines.

It is intended to give humans and machines a shared intermediate layer through which meaning can be negotiated, translated, executed, and revised.

## Next

1. Recover and formalize the original manifesto.
2. Define the minimum shared vocabulary.
3. Define the message protocol.
4. Build a working translation pipeline.
5. Test it against real human-machine interactions.
