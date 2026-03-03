<script lang="ts">
    import {goto} from "$app/navigation";

    let email = $state('');
    let username = $state('');
    let password = $state('');

    let error = $state('');
    let loading = $state(false);

    let isValid = $derived(
        email && password
    );

    async function handleSubmit(event: SubmitEvent){
        event.preventDefault();

        if(!isValid){
            error = "Something Wrong";
            return
        }

        loading = true;

        // setTimeout( () => {
        //     console.log(` email : ${email}\n password : ${password}`);
        //     loading = false;
        // }, 1000);
        
        try {
            const resp = await fetch(
                "http://127.0.0.1:8000/login",
                {
                    method : "POST",
                    headers : {
                        "Content-Type" : "application/json",
                    },
                    body : JSON.stringify({ email, password})
                }
            );

            const data = await resp.json();

            if(!resp.ok){
                error = data.detail || "Login Failed";
            } else {
                localStorage.setItem("shopit_token", data.access_token);
                await goto("/");
            }
        }
        catch(err){
            error = "Server not reachable";
        }

        loading = false;

    }

</script>

<div class="min-h-screen bg-gray-100 flex justify-center items-center">
    <div class="w-full max-w-md shadow-lg bg-white p-8 rounded-2xl">
        <h1 class="text-3xl font-bold text-center mb-6">Let's ShopIt</h1>

        {#if error}
            <p class="text-red-500 text-sm mb-4">{error}</p>
        {/if}

        <form onsubmit={handleSubmit} class="flex flex-col space-y-4">
            <input type="email" bind:value={email} class="rounded-lg py-2 px-4 focus:border-black focus:ring-black focus:ring-2"/>
            <input type="password" bind:value={password} class="rounded-lg py-2 px-4 focus:border-black focus:ring-black focus:ring-2"/>
            <button
                type="submit"
                // disabled={!isValid || loading}
                class="bg-black text-white py-2 rounded-lg disabled:opacity-50"
            >
            { loading ? "Loging in ... " : "Log In"} 
            </button>
        </form>
    </div>
</div>