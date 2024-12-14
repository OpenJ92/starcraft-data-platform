class PLAYER(db.Model):
    __tablename__ = "PLAYER"
    __table_args__ = {"schema": "replay"}

    __id__ = db.Column(db.Integer, primary_key=True)

    sid = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    is_human = db.Column(db.Boolean)
    is_observer = db.Column(db.Boolean)
    is_referee = db.Column(db.Boolean)
    region = db.Column(db.Text)
    subregion = db.Column(db.Integer)
    toon_id = db.Column(db.BigInteger)
    uid = db.Column(db.Integer)
    clan_tag = db.Column(db.Text)
    name = db.Column(db.Text)
    combined_race_levels = db.Column(db.BigInteger)
    highest_league = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    result = db.Column(db.Text)
    pick_race = db.Column(db.Text)
    play_race = db.Column(db.Text)

    id = db.Column(db.Integer)

    objects = db.relationship( "OBJECT", primaryjoin="OBJECT.__OWNER__==PLAYER.__id__", back_populates="owner")

    __INFO__ = db.Column(db.Integer, db.ForeignKey("replay.INFO.__id__"))
    replay = db.relationship("INFO", back_populates="players")
