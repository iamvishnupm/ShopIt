<script lang="ts">
	import { currentUser } from '$lib/stores/auth';
	import ProfileButton from './profile_button.svelte';
	import MenuButton from './menu_button.svelte';

	import Logo from '$lib/icons/logo.svelte';
	import MicIcon from '$lib/icons/mic_icon.svelte';
	import SearchIcon from '$lib/icons/search_icon.svelte';

	let menuOpen = $state(false);

	function toggleMenu() {
		menuOpen = !menuOpen;
	}

	const links = ['First Link', 'Second Link', 'Third Link', 'Fourth Link'];
</script>

<header
	class="body-font container mx-auto flex flex-col p-10 text-gray-600 lg:flex-row lg:items-center lg:justify-between"
>
	<!-- logo & navigations -->
	<div class="mb-8 flex flex-col md:flex-row md:justify-between md:space-x-10 lg:mb-0">
		<div class="flex items-center">
			<div class="title-font flex cursor-pointer font-medium text-gray-900">
				<Logo />
				<span class="ml-3 text-xl">ShopIt</span>
			</div>

			<div class="flex w-full items-center justify-end space-x-5 md:hidden">
				<MenuButton {menuOpen} toggle={toggleMenu} />
				<ProfileButton height={18} width={20} addClass="mt-0.5" />
			</div>
		</div>

		<nav
			class={`${menuOpen ? 'mb-4 flex' : 'hidden'} mt-12 flex-col space-y-5 pl-2 md:mt-0 md:mb-0 md:flex md:flex-row md:items-center md:justify-center md:space-y-0 md:pl-0`}
		>
			{#each links as link}
				<span
					class="w-full cursor-pointer border-b border-gray-300 pb-2 hover:text-gray-900 md:mr-5 md:w-fit md:border-0 md:pb-0"
				>
					{link}
				</span>
			{/each}
		</nav>

		<ProfileButton height={18} width={20} addClass="hidden self-end md:flex lg:hidden" />
	</div>

	<!-- search box -->
	<div class="flex">
		<div class="relative w-full lg:w-fit">
			<SearchIcon addClass="absolute top-3 left-4 text-gray-400" />
			<MicIcon addClass="absolute top-3 right-4 cursor-pointer text-blue-500" />
			<input
				class="w-full rounded-full border p-2.5 pl-10 hover:shadow-lg focus:shadow-lg focus:outline-0"
				type="text"
				placeholder="Search Items"
			/>
		</div>

		<ProfileButton height={24} width={28} addClass="hidden lg:ml-5 lg:flex" />
	</div>
</header>
