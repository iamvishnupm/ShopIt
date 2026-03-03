<script>
    import {goto} from "$app/navigation";
    import {onMount} from "svelte";

    onMount(
        async () => {
            const token = localStorage.getItem("shopit_token");

            if(!token){
                goto("/login");
            }

            try {
                const resp = await fetch(
                    "http://127.0.0.1:8000/me",
                    {
                        headers : {
                            "Authorization" : `Bearer ${token}`
                        }
                    }
                );

                if(!resp.ok){
                    localStorage.removeItem("shopit_token");

                    console.log("Error");
                    console.log(resp);

                    goto("/login");
                }
            }
            catch(err) {
                console.log(err);
            }
        }
    );
</script>

<h1>ShopIt</h1>
