<script lang="ts">
	import { getContext, onMount } from 'svelte';
	import { toast } from 'svelte-sonner';
	import dayjs from 'dayjs';

	import { getAllMemories } from '$lib/apis/memories';

	const i18n = getContext('i18n');

	let memories = [];
	let loaded = false;

	onMount(async () => {
		memories = await getAllMemories(localStorage.token).catch((error) => {
			toast.error(`${error}`);
			return [];
		});
		loaded = true;
	});
</script>

<div class="flex flex-col gap-1 py-2">
	<div class="text-lg font-medium px-0.5">{$i18n.t('Memories')}</div>
	<div class="text-xs text-gray-500 px-0.5 mb-2">
		{$i18n.t('Memories saved by every user on this instance.')}
	</div>

	{#if loaded && memories.length === 0}
		<div class="text-sm text-gray-500 px-0.5">{$i18n.t('No memories yet.')}</div>
	{:else}
		<table class="w-full text-sm text-left">
			<thead class="text-xs text-gray-500 uppercase">
				<tr>
					<th class="py-1.5 pr-3">{$i18n.t('User')}</th>
					<th class="py-1.5 pr-3">{$i18n.t('Memory')}</th>
					<th class="py-1.5">{$i18n.t('Updated')}</th>
				</tr>
			</thead>
			<tbody>
				{#each memories as memory (memory.id)}
					<tr class="border-t border-gray-100 dark:border-gray-850">
						<td class="py-1.5 pr-3 whitespace-nowrap">{memory.user_id}</td>
						<td class="py-1.5 pr-3">{memory.content}</td>
						<td class="py-1.5 whitespace-nowrap">
							{dayjs(memory.updated_at * 1000).format('YYYY-MM-DD HH:mm')}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{/if}
</div>
