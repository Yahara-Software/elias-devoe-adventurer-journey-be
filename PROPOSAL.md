## Proposal: plan for development

### Minimal Choices:
1. Get the final distance asked for in the spec
1. Different initial starting direction
1. Different allowed directions
1. If changing direction of adventurer, map codes such that they mean the same thing
1. Save state
1. Handle malformed inputs


### Initial Development Plan
1. Architecture: Clean Code (Controller -> Use Case -> Service -> Model)
1. Set up docker environment: fastapi, db, frontend
1. Code up minimal choices
1. Tests and mock data


## Secondary Development Options
1. Metadata (time, etc.)
1. Auth/users
1. Decide how to view; async timed producer loop so moves are visualized as the backend emits new locations, or only end state?
1. Mock frontend interface consuming the API