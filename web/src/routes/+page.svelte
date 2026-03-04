<script>
	import { onMount } from 'svelte';

	import { currentUser } from '$lib/stores/auth';
	import { initializeSession } from '$lib/auth/session';

	// components

	import Header from '$lib/components/header.svelte';

	// ========================================================

	onMount(async () => await initializeSession());

	// ========================================================
</script>

<div class="min-h-screen bg-gray-50">
	<Header />
</div>
