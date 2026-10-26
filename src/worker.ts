import handler, { createScheduledHandler, PluginBridge } from "@emdash-cms/cloudflare/worker";

export { PluginBridge };

// Affiliate link hosts. Links to these get rel="sponsored nofollow noopener" so search
// engines treat them as paid links (Google's recommendation for affiliate links).
const AFFILIATE_HREF =
	/^https?:\/\/([a-z0-9-]+\.)*(amazon\.com|amzn\.to|hb\.afl\.rakuten\.co\.jp)(\/|$)/i;

const REQUIRED_REL = ["sponsored", "nofollow", "noopener"];

function markAffiliateLinks(response: Response): Response {
	const type = response.headers.get("content-type") ?? "";
	if (!type.includes("text/html")) return response;
	return new HTMLRewriter()
		.on("a[href]", {
			element(el) {
				const href = el.getAttribute("href");
				if (!href || !AFFILIATE_HREF.test(href)) return;
				const rel = new Set((el.getAttribute("rel") ?? "").split(/\s+/).filter(Boolean));
				for (const value of REQUIRED_REL) rel.add(value);
				el.setAttribute("rel", [...rel].join(" "));
			},
		})
		.transform(response);
}

export default {
	...handler,
	async fetch(request, env, ctx) {
		const response = await handler.fetch!(request, env, ctx);
		// Leave the admin app and API responses untouched.
		if (new URL(request.url).pathname.startsWith("/_emdash")) return response;
		return markAffiliateLinks(response);
	},
	scheduled: createScheduledHandler(),
} satisfies ExportedHandler;
