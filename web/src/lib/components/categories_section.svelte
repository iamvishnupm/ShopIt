<script lang="ts">
	let categories = [
		{ name: 'Electronics', image: 'https://picsum.photos/200?random=1' },
		{ name: 'Fashion', image: 'https://picsum.photos/200?random=2' },
		{ name: 'Home', image: 'https://picsum.photos/200?random=3' },
		{ name: 'Books', image: 'https://picsum.photos/200?random=4' },
		{ name: 'Sports', image: 'https://picsum.photos/200?random=5' },
		{ name: 'Gaming', image: 'https://picsum.photos/200?random=6' }
	];
</script>

<div class="px-6 py-6">
	<div
		class="grid grid-cols-2 place-items-center gap-6 sm:grid-cols-3 md:grid-cols-5 lg:grid-cols-6"
	>
		{#each categories as c}
			<div class="flex cursor-pointer flex-col items-center">
				<img
					src={c.image}
					alt={c.name}
					class="aspect-square w-full max-w-30 rounded-lg object-cover shadow-sm"
				/>

				<span class="mt-2 text-center text-sm text-gray-700">
					{c.name}
				</span>
			</div>
		{/each}
	</div>
</div>
