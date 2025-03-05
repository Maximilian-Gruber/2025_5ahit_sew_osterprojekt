import request from './req';
import axios from 'axios';

export const apiGetTeamsList = () => axios.get('/teams');
export const apiGetTeam = (id) => axios.get(`/teams/${id}`);
export const apiCreateTeam = data => axios.post('/teams', data);
export const apiDeleteTeam = (id) => axios.delete(`/teams/${id}`);
export const apiAddPlayerToTeam = (teamId, playersId) => axios.post(`/teams/${teamId}/players/${playersId}`);
export const apiGetPlayersPerTeam = (teamId) => axios.get(`/teams/${teamId}/players`);