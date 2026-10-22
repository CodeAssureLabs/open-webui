import { get } from 'svelte/store';

import { user, WEBUI_NAME } from '../stores';

/** Label shown in the window title: "<name> · <app>" or just the app name. */
export const sessionLabel = (): string => {
	const current = get(user);
	const app = get(WEBUI_NAME);
	return current?.name ? `${current.name} · ${app}` : app;
};
