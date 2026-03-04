<script lang="ts">
	let { height = 24, width = 24, addClass = '' } = $props();
</script>

<button
	class={`flex cursor-pointer items-center justify-center rounded-full border border-gray-300 p-2 hover:bg-gray-100 ${addClass}`}
	aria-label="Profile"
>
	<svg
		xmlns="http://www.w3.org/2000/svg"
		{height}
		{width}
		fill="none"
		viewBox="0 0 24 24"
		stroke="currentColor"
		class="text-gray-700"
	>
		<path
			stroke-linecap="round"
			stroke-linejoin="round"
			stroke-width="2"
			d="M5.121 17.804A9 9 0 1118.879 17.804M15 11a3 3 0 11-6 0 3 3 0 016 0z"
		/>
	</svg>
</button>
