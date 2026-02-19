class Solution:
    def matchPlayersAndTrainers(
        self, players: list[int], trainers: list[int]
    ) -> int:
        players.sort()
        trainers.sort()
        happy = 0
        pi = ti = 0
        while pi < len(players) and ti < len(trainers):
            p = players[pi]
            t = trainers[ti]
            if p <= t:
                happy += 1
                pi += 1
            ti += 1
        return happy
