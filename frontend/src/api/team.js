import request from './req';
import axios from 'axios';

export const apiGetTeamsList = (access_token) => axios.get('/teams', { headers: { "Authorization": `Bearer ${access_token}`, "Content-Type": "application/json" }});
export const apiGetTeam = (id, access_token) => axios.get(`/teams/${id}`, { headers: { "Authorization": `Bearer ${access_token}`, "Content-Type": "application/json" }});
export const apiCreateTeam = (data, access_token) => axios.post('/teams', data, { headers: { "Authorization": `Bearer ${access_token}`, "Content-Type": "application/json" }});
export const apiDeleteTeam = (id) => axios.delete(`/teams/${id}`);
export const apiAddPlayerToTeam = (teamId, playerId) => axios.post(`/teams/${teamId}/players/${playerId}`);
export const apiGetPlayersPerTeam = (teamId) => axios.get(`/teams/${teamId}/players`);