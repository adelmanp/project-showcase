# Project Showcase

This repository is a curated collection of programming projects that showcase my work across Python applications, small games, utilities, graphics exercises, infrastructure-as-code examples.

The current projects are primarily Python-based and were selected from earlier learning repositories, then reorganized into a single portfolio so they are easier to review as code samples. Over time, this repo will also include additional infrastructure automation examples and AI/API exercises built in Python notebooks.

## Skills Demonstrated

- Python fundamentals
- Control flow and input validation
- Functions and modular code organization
- Game and application state management
- Working with files and supporting modules
- Simple GUI and graphics with `turtle`
- Infrastructure as code with Terraform
- Basic AWS provisioning and cloud-init bootstrapping

## Featured Projects

| Project | Category | Summary | Run |
| --- | --- | --- | --- |
| `adventure-game` | CLI game | Text adventure with branching paths, replay flow, and randomized starting conditions. | `python3 projects/cli-games/adventure-game/main.py` |
| `hangman` | CLI game | Multi-file word guessing game with supporting art and word list modules. | `python3 projects/cli-games/hangman/hangman.py` |
| `blackjack` | CLI game | Blackjack implementation with score calculation, dealer logic, and repeated rounds. | `python3 projects/cli-games/blackjack/blackjack.py` |
| `high-low-game` | CLI game | Comparison game using external data and loop-based score tracking. | `python3 projects/cli-games/high-low-game/main.py` |
| `coffee-machine` | Utility simulation | Simulates drink ordering, payment handling, inventory checks, and change logic. | `python3 projects/utilities/coffee-machine/main.py` |
| `password-generator` | Utility | Generates randomized passwords based on user-selected character counts. | `python3 projects/utilities/password-generator/main.py` |
| `turtle-race` | Graphics | Interactive turtle-race game with user input and randomized movement. | `python3 projects/graphics/turtle-race/turtle_race.py` |
| `snake-game` | Graphics | Snake game with collision detection, score tracking, and keyboard controls. | `python3 projects/graphics/snake-game/main.py` |
| `pong` | Graphics | Pong clone built with object-oriented components and keyboard controls. | `python3 projects/graphics/pong/pong.py` |
| `ec2-apache` | IaC / Terraform | Provisions an AWS EC2 instance and bootstraps Apache with cloud-init. | `cd projects/iac/terraform/ec2-apache && terraform init && terraform apply` |

## Repository Structure

```text
projects/
  cli-games/
  utilities/
  graphics/
  iac/
    terraform/
```

## Notes

- These examples use the Python standard library. The graphics projects use `turtle`, which requires a desktop environment.
- Each project folder includes a short README with context and run instructions.
- A few folders also include closely related alternate implementations or practice sketches that are documented in their local README files.
- Infrastructure examples are organized under `projects/iac/` so additional tools such as CDK can be added later without reshaping the repo.
