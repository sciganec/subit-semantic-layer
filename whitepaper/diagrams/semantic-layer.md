```mermaid
flowchart TB
    %% SEMANTIC LAYER STACK

    subgraph FOUNDATION[ ]
        direction TB
        T[MIST-Theory<br><sub>Minimal Information Subjectivity Theory</sub>]:::theory
    end

    subgraph ONTOLOGY[ ]
        direction TB
        O[SUBIT‑64 Ontology<br><sub>64 Archetypal States + Shadow Axes</sub>]:::ontology
    end

    subgraph ENGINE[ ]
        direction TB
        M[MIST‑Engine<br><sub>Modular Interpretive Structured Thinking</sub>]:::engine
    end

    subgraph TOPOLOGY[ ]
        direction TB
        C[Content Topology Layer<br><sub>Semantic Manifold / Graph</sub>]:::topology
    end

    subgraph MASKS[ ]
        direction TB
        B[Behavioral Masks<br><sub>Persona / Role / Constraints</sub>]:::masks
    end

    subgraph OUTPUT[ ]
        direction TB
        A[Agent Output<br><sub>Stable, Interpretable Behavior</sub>]:::output
    end

    T --> O --> M --> C --> B --> A

    classDef theory fill:#dde6ff,stroke:#333,stroke-width:1px,color:#000
    classDef ontology fill:#6fa8dc,stroke:#333,stroke-width:1px,color:#000
    classDef engine fill:#b4a7d6,stroke:#333,stroke-width:1px,color:#000
    classDef topology fill:#f6b26b,stroke:#333,stroke-width:1px,color:#000
    classDef masks fill:#eeeeee,stroke:#333,stroke-width:1px,color:#000
    classDef output fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
