from pydantic import BaseModel, field_serializer


class Profile(BaseModel):
    account_id: int
    personaname: str | None
    name: str | None
    plus: bool
    cheese: int | None
    steamid: str | None
    avatar: str | None
    avatarmedium: str | None
    avatarfull: str | None
    profileurl: str | None
    last_login: str | None
    loccountrycode: str | None
    status: bool | None
    fh_unavailable: bool
    is_contributor: bool
    is_subscriber: bool


class PlayerData(BaseModel):
    profile: Profile
    rank_tier: int | None
    leaderboard_rank: int | None


class WinratePlayer(BaseModel):
    win: int | None
    lose: int | None

