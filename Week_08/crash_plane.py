'''
run a MCMC simulation for places.
'''
from random import choices

STATES = ['airport', 'air', 'crashed']

def mcmc(state, transition_probs):
    '''
    runs a Monte-Carlo Markov-Chain simulation of a place.
    Returns a list of states passed.
    '''
    history = [state]
    while state != 'crashed':
        probs = transition_probs[state]
        state = choices(STATES, probs)[0]
        history.append(state)
    return list

P = {
    'airport': [0.4, 0.6, 0.0],
    'air': [0.8, 0.19999, 0.00001],
}
print(f"crashed after {len(mcmc('airport', P))} days of service")
