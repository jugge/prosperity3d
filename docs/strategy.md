# Strategiarkitektur

Det här dokumentet beskriver de centrala klasserna i strategimotorn för TrueProsperity-projektet.

```mermaid
classDiagram
  class StrategyBase {
    +run(data)
    +evaluate() : float
    +get_results() : Result
  }

  class SavingsStrategy
  class RiskyStrategy
  class InputData
  class Result

  StrategyBase <|-- SavingsStrategy
  StrategyBase <|-- RiskyStrategy
  StrategyBase --> Result
  StrategyBase --> InputData
