---
name: Question
about: Describe this issue template's purpose here.
title: ''
labels: question
assignees: ''

---

When your question is related to code that isn't working as expected, please enable debug logs:

``` python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Also start [the event loop](https://docs.python.org/3/library/asyncio-dev.html#debug-mode) in debug mode. 

If these actions didn't help to find the cause of your issue, please provide code samples and logs with your question.
