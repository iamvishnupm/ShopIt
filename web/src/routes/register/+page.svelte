<script lang="ts">
	let email = $state('');
	let username = $state('');
	let password = $state('');
	let confirmPassword = $state('');

	let error = $state('');
	let loading = $state(false);

	let isValid = $derived(
		email && username && password && confirmPassword && password === confirmPassword
	);

	async function handleSubmit(event: SubmitEvent) {
		event.preventDefault();

		if (!isValid) {
			error = 'Fix the form';
			return;
		}

		error = '';
		loading = true;

		// setTimeout(() => {
		// 	console.log(` email : ${email}\n username : ${username}\n password : ${password}`);
		// 	loading = false;
		// }, 1000);

		try {
			const resp = await fetch(
				"http://127.0.0.1:8000/register",
				{
					method : "POST",
					headers : {
						"Content-Type" : "application/json"
					},
					body : JSON.stringify({
						email, username, password
					})
				}
			);

			const data = await resp.json();

			if(!resp.ok) {
				error = data.detail || "Registration Failed";
			} 
			else {
				alert("Account Created")
				console.log("Account Details");
				console.log(data);
			}
		} 
		catch(err) {
			error = "Server not reachable";
		}

		loading = false;
	}
</script>

<div class="flex min-h-screen items-center justify-center bg-gray-100">
	<div class="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg">
		<h1 class="mb-6 text-center text-3xl font-bold">Create Accouont</h1>

		{#if error}
			<p class="mb-4 text-sm text-red-500">{error}</p>
		{/if}

		<form onsubmit={handleSubmit} class="flex flex-col space-y-4">
			<input
				type="email"
				bind:value={email}
				class="rounded-lg border px-4 py-2 focus:ring-2 focus:ring-black"
			/>
			<input
				type="text"
				bind:value={username}
				class="rounded-lg border px-4 py-2 focus:ring-2 focus:ring-black"
			/>
			<input
				type="password"
				bind:value={password}
				class="rounded-lg border px-4 py-2 focus:ring-2 focus:ring-black"
			/>
			<input
				type="password"
				bind:value={confirmPassword}
				class="rounded-lg border px-4 py-2 focus:ring-2 focus:ring-black"
			/>

			<button
				type="submit"
				// disabled={!isValid || loading}
				class="rounded-lg bg-black py-2 text-white disabled:opacity-50"
			>
				{loading ? 'Creating . . .' : 'Register'}
			</button>
		</form>
	</div>
</div>
