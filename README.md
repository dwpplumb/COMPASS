# COMPASS

[![Open Collective](https://img.shields.io/opencollective/all/compass?label=Backers&color=blue)](https://opencollective.com/compass)
[![GitHub stars](https://img.shields.io/github/stars/dwpplumb/COMPASS?style=social)](https://github.com/dwpplumb/COMPASS)

COMPASS is an axiomatic reasoning engine and value system based on universal logical and physical principles. The core goal is to create a system that can evaluate input, generate reasoning paths, and provide structured outputs based on fundamental axioms. COMPASS is modular, extensible, and designed for integration with both classical and LLM-driven architectures (e.g., via Metacortex or Ollama backends).

## Features

* Axiomatic value assessment based on a defined axiom set
* Modular codebase with clear separation of logic, LLM-interfaces, and evaluation
* FastAPI backend for programmatic interaction
* Ready for containerized deployment (Docker)
* Prepared for integration with vector models, FNet-style word analysis, and superposition routines

## Repository Structure

```
core/
    evaluator.py        # Core logic for evaluating user input and mapping to axioms
    llm_interface.py    # Handles LLM/cognitive system interactions
    ...
main.py                # FastAPI app entrypoint
Dockerfile.compass      # Docker build configuration
requirements.txt        # Python dependencies
README.md               # This file
```

## Quickstart

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dwpplumb/COMPASS.git
   cd COMPASS
   ```
2. **Install requirements:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## Docker Usage

Edit and use the provided Dockerfile.compass and docker-compose.yml to build and run COMPASS together with related containers (e.g., frontend or Metacortex).

## Example API Call

```
POST /evaluate/
{
  "text": "What is existence?"
}
Response:
{
  "result": ...
}
```

## Principles

* **Axiomatic Consistency:** Every response is mapped to a defined axiom or subaxiom.
* **Extendability:** New axioms, evaluation modules, and LLM backends can be added modularly.
* **Transparency:** All evaluation paths and outputs are documented and reproducible.

## License

MIT License (recommendation)

## Contact


Project by David Plumb / COMPASS System Architecture

- [GitHub Repository](https://github.com/dwpplumb/COMPASS)
- [OpenCollective (Support & Community)](https://opencollective.com/compass)

**Project Board:** [COMPASS GitHub Project](https://github.com/dwpplumb/COMPASS/projects)

