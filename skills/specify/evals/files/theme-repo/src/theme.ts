export type Theme = "light" | "dark";

export function resolveTheme(selected: Theme): "light" | "dark" {
  return selected;
}
