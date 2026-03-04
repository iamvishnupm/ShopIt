<script lang="ts">
	let { menuOpen = false, toggle, addClass = 'h-6 w-6' } = $props();
</script>

<button class="cursor-pointer md:hidden" aria-label="hamburger" onclick={toggle}>
	{#if menuOpen}
		<!-- Close icon -->
		<svg
			xmlns="http://www.w3.org/2000/svg"
			class={`${addClass}`}
			fill="none"
			viewBox="0 0 24 24"
			stroke="currentColor"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M6 18L18 6M6 6l12 12"
			/>
		</svg>
	{:else}
		<!-- Hamburger icon -->
		<svg
			xmlns="http://www.w3.org/2000/svg"
			class={`${addClass}`}
			fill="none"
			viewBox="0 0 24 24"
			stroke="currentColor"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M4 6h16M4 12h16M4 18h16"
			/>
		</svg>
	{/if}
</button>
