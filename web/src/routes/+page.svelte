<script>
    import {goto} from "$app/navigation";
    import {onMount} from "svelte";

    import {currentUser} from "$lib/stores/auth";

    onMount(
        async () => {
            const token = localStorage.getItem("shopit_token");

            if(!token){
                goto("/login");
            }

            try {
                const resp = await fetch("http://127.0.0.1:8000/me", {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                });

                if (!resp.ok) {
                    localStorage.removeItem("shopit_token");
                    await goto("/login");
                    return;
                }

                const user = await resp.json();

                console.log("Authenticated user:", user);

                // storing user details for future use.
                currentUser.set(user);

                console.log("User details saved");

            } catch (err) {
                console.error("Auth check failed:", err);
                localStorage.removeItem("shopit_token");
                await goto("/login");
            }
        }
    );


</script>

<h1>ShopIt</h1>
{#if $currentUser}
  <p>username : {$currentUser.username}</p>
  <p>email : {$currentUser.email}</p>
{/if}
