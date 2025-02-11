# Prompt Injection Scanner

It is specifically tailored to guard against crafty input manipulations targeting large
language models (LLM). By identifying and mitigating such attempts, it ensures the LLM operates securely without
succumbing to injection attacks.

## Attack

Injection attacks, especially in the context of LLMs, can lead the model to perform unintended actions. There are two
primary ways an attacker might exploit:

- **Direct Injection**: Directly overwrites system prompts.

- **Indirect Injection**: Alters inputs coming from external sources.

!!! info

    As specified by the `OWASP Top 10 LLM attacks`, this vulnerability is categorized under:

    [LLM01: Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - It's crucial to
    monitor and validate prompts rigorously to keep the LLM safe from such threats.

## How it works

It leverages the
model [JasperLS/deberta-v3-base-injection](https://huggingface.co/JasperLS/deberta-v3-base-injection) for its operation.
However, it's worth noting that while the current model can detect attempts effectively, it might occasionally yield
false positives.

!!! warning

    Due to this limitation, one should exercise caution when considering its deployment in a production
    environment.

While the dataset is nascent, it can be enriched, drawing from repositories of known attack patterns, notably
from platforms like [JailbreakChat](https://www.jailbreakchat.com/).

## Usage

```python
from llm_guard.input_scanners import PromptInjection

scanner = PromptInjection(threshold=0.5)
sanitized_prompt, is_valid, risk_score = scanner.scan(prompt)
```
