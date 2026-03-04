<script lang="ts">
	import { onMount } from 'svelte';

	let { variant = 'large' } = $props();

	let ads = [
		'https://picsum.photos/1200/300?random=1',
		'https://picsum.photos/1200/300?random=2',
		'https://picsum.photos/1200/300?random=3'
	];

	let index = $state(0);

	function goTo(i: number) {
		index = i;
	}

	onMount(() => {
		const interval = setInterval(
			() => {
				index = (index + 1) % ads.length;
			},
			variant === 'large' ? 4000 : 7000
		);

		return () => clearInterval(interval);
	});
</script>

<div class="px-6 py-4">
	<!-- viewport -->
	<div class="overflow-hidden rounded-xl">
		<!-- sliding container -->
		<div
			class="flex transition-transform duration-700"
			style={`transform: translateX(-${index * 100}%);`}
		>
			{#each ads as ad}
				<img
					src={ad}
					class={`w-full flex-shrink-0 object-cover ${variant === 'large' ? 'h-64' : 'h-40'}`}
				/>
			{/each}
		</div>
	</div>

	<!-- dots -->
	<div class="mt-3 flex justify-center gap-2">
		{#each ads as _, i}
			<button
				class={`h-2 w-2 rounded-full transition ${i === index ? 'bg-gray-800' : 'bg-gray-400'}`}
				onclick={() => goTo(i)}
			></button>
		{/each}
	</div>
</div>
