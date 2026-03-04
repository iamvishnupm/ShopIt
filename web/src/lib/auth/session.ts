import { goto } from '$app/navigation';
import { currentUser } from '$lib/stores/auth';

export async function initializeSession() {
	const token = localStorage.getItem('shopit_token');

	if (!token) {
		await goto('/login');
		return null;
	}

	try {
		const resp = await fetch('http://127.0.0.1:8000/me', {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});

		if (!resp.ok) {
			localStorage.removeItem('shopit_token');
			await goto('/login');
			return null;
		}

		const user = await resp.json();

		// storing user details for future use.
		currentUser.set(user);

		return user;
	} catch (err) {
		console.error('Auth check failed : ', err);
		localStorage.removeItem('shopit_token');
		await goto('/login');
		return null;
	}
}
