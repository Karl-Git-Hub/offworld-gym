# Copyright offworld.ai 2019

from gym.envs.registration import register

# Real environments

# OffWorld Monolith Real 
register(
    id='OffWorldMonolithDiscreteReal-v0',
    entry_point='offworld_gym.envs.real:OffWorldMonolithDiscreteEnv'
)

# simulated environments

# OffWorld Monolith Simulated replica with discrete actions
register(
    id='OffWorldMonolithDiscreteSim-v0',
    entry_point='offworld_gym.envs.gazebo:OffWorldMonolithDiscreteEnv'

# OffWorld Monolith Simulated replica with continous actions
register(
    id='OffWorldMonolithDiscreteSim-v0',
    entry_point='offworld_gym.envs.gazebo:OffWorldMonolithContinousEnv'
)