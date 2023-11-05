from dataclasses import dataclass


@dataclass
class CreateSkillOfferResponseDto:
    id: int
    oferta_id: int
    skill_id: int
    dominio: int

