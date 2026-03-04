<script lang="ts">
	import { currentUser } from '$lib/stores/auth';
</script>

<header class="flex items-center justify-between bg-white px-6 py-4 shadow-sm">
	<div class="text-2xl font-bold text-blue-600">ShopIt</div>

	<nav class="flex gap-6 text-gray-700">
		<a href="/">Home</a>
		<a href="/orders">Orders</a>
		<a href="/cart">Cart</a>
	</nav>
</header>
