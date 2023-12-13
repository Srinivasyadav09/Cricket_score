class Cricket:
    def __init__(self, match_bw,status=" ", matchtype="Unknown", team1="Team A",team2="Team B", t1_runs=0, t1_wickets=0, t1_overs=0
                 , t2_runs=0, t2_wickets=0, t2_overs=0, ):
        self.match_bw = str(match_bw)
        self.team_1 = str(team1)
        self.t1_runs = str(t1_runs)
        self.t1_wickets = str(t1_wickets)
        self.t1_overs = str(t1_overs)
        self.team_2 = str(team2)
        self.t2_runs = str(t2_runs)
        self.t2_wickets = str(t2_wickets)
        self.t2_overs = str(t2_overs)
        self.match_status = str(status)
        self.match_type = str(matchtype)

    def structuring(self):
        while len(self.team_1) < 36:
            self.team_1 += " "
        while len(self.t1_runs + "/" + self.t1_wickets) < 30:
            self.t1_wickets += " "
        while len(self.t1_overs) < 30:
            self.t1_overs += " "

    def Current_Matches(self):
        print(
            f' *********************************************************** {self.match_bw} *******************************************************   ',
            "\n")
        print(f"         {self.match_type.upper()}")
        print(f"                    {self.team_1}||              {self.team_2}                    ")
        print(
            f"                    Score:{self.t1_runs}/{self.t1_wickets}||              Score:{self.t2_runs}/{self.t2_wickets}")
        print(f"                    Overs:{self.t1_overs}||              Overs:{self.t2_overs}")
        print(f'         {self.match_status}\n')
