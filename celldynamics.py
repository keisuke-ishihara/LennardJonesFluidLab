from classes import Ensemble

def CellDynamics(coords_over_time, ensembleArgs):
    '''
    Parameters
    ----------
    coords_over_time : list of 2D numpy arrays
        Stores the x-y coordinates.
    ensembleArgs : dictionary
        Specifies the keyword arguments for the Ensemble class.   

    Returns ensembles, a list of Ensembles.
    -------
    '''   
    
    N = []
    PE = []
    ens_for_traj = Ensemble(nMol=len(coords_over_time[-1]), **ensembleArgs)
    for positions in coords_over_time:
        ensemble = Ensemble(nMol=len(positions), **ensembleArgs)
        for i, mol in enumerate(ensemble.moList):
            mol.r = positions[i]
        N.append(len(positions))
        PE.append(ensemble.getPE())
        ens_for_traj.trajectory.append(positions)
    
    # update the positions in the ensemble to be returned
    for i, mol in enumerate(ens_for_traj.moList):
            mol.r = positions[i]
            
    # remove the first entry in the trajectory
    ens_for_traj.trajectory = ens_for_traj.trajectory[1:]
    
    return N, PE, ens_for_traj
