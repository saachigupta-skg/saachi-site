// Shared loader for the auto-generated index pages (builds, learnings,
// reflections, adventures). Each index page passes in its own
// import.meta.glob results, since glob paths must be static.

export type Entry = {
  url: string;
  slug: string;
  title: string;
  date: string;
  excerpt: string;
  tags: string[];
  readTime: string;
  link: string;
  location: string;
  activityType: string;
  distance: string;
  elevation: string;
  coverImage: string;
};

function estimateReadTime(raw: string): string {
  const body = raw
    .replace(/^---[\s\S]*?---\n?/, "")
    .replace(/<[^>]+>/g, " ")
    .replace(/\{[^}]*\}/g, " ");
  const words = body.trim().split(/\s+/).filter((w) => w.length > 1).length;
  return `${Math.max(1, Math.ceil(words / 200))} min read`;
}

export function loadEntries(
  section: string,
  modules: Record<string, any>,
  rawModules: Record<string, string> = {},
): Entry[] {
  return Object.entries(modules)
    // Skip the index itself and underscore-prefixed files (templates, not routes).
    .filter(([path]) => !path.endsWith("/index.astro") && !path.startsWith("./_"))
    .map(([path, mod]) => {
      const slug = path.replace("./", "").replace(".astro", "");
      return {
        url: `/${section}/${slug}`,
        slug,
        title: mod.title ?? slug.replaceAll("-", " "),
        date: mod.date ?? "",
        excerpt: mod.excerpt ?? "",
        tags: Array.isArray(mod.tags) ? mod.tags : [],
        readTime: rawModules[path] ? estimateReadTime(rawModules[path]) : "",
        link: mod.link ?? "",
        location: mod.location ?? "",
        activityType: mod.activityType ?? "",
        distance: mod.distance ?? "",
        elevation: mod.elevation ?? "",
        coverImage: mod.coverImage ?? "",
      };
    })
    .sort((a, b) => (b.date || "").localeCompare(a.date || ""));
}
