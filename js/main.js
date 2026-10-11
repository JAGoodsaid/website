/* Progressive enhancement: all content and contact links work without JavaScript. */
'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
const mobile = window.matchMedia('(max-width: 800px)');
function syncMenu() {
  menuButton.hidden = !mobile.matches;
  menuButton.setAttribute('aria-expanded', 'false');
  navigation.classList.toggle('mobile-closed', mobile.matches);
}
syncMenu();
mobile.addEventListener('change', syncMenu);
menuButton.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!expanded));
  navigation.classList.toggle('mobile-closed', expanded);
});
navigation.addEventListener('click', event => {
  if (event.target.closest('a') && mobile.matches) syncMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && mobile.matches && menuButton.getAttribute('aria-expanded') === 'true') {
    syncMenu();
    menuButton.focus();
  }
});
const filters = document.querySelector('.filters');
const projects = [...document.querySelectorAll('.project')];
filters.hidden = false;
filters.addEventListener('click', event => {
  const button = event.target.closest('button[data-filter]');
  if (!button) return;
  const selected = button.dataset.filter;
  filters.querySelectorAll('button').forEach(item => {
    const active = item === button;
    item.classList.toggle('active', active);
    item.setAttribute('aria-pressed', String(active));
  });
  let count = 0;
  projects.forEach(project => {
    const visible = selected === 'all' || project.dataset.category.split(' ').includes(selected);
    project.hidden = !visible;
    if (visible) count++;
  });
  document.querySelector('#filter-status').textContent = `${count} ${count === 1 ? 'project' : 'projects'} shown`;
});
document.querySelector('#year').textContent = new Date().getFullYear();

// Count career statistics once when the section enters the viewport.
// Keep the HTML's final values as the no-JavaScript / reduced-motion fallback.
(() => {
  const section = document.querySelector('.stats');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!section || reducedMotion.matches || !('IntersectionObserver' in window)) return;

  const counters = [...section.querySelectorAll('strong')].map(element => {
    const finalText = element.textContent.trim();
    const match = finalText.match(/^(\d+)(.*)$/);
    if (!match) return null;
    // Screen readers receive the final number, not every animation frame.
    const accessible = document.createElement('span');
    accessible.className = 'sr-only';
    accessible.textContent = finalText;
    const visual = document.createElement('span');
    visual.className = 'counter-value';
    visual.setAttribute('aria-hidden', 'true');
    visual.textContent = finalText;
    element.replaceChildren(accessible, visual);
    return { visual, target: Number(match[1]), suffix: match[2], finalText };
  }).filter(Boolean);

  const duration = 1600; // Animation length in milliseconds.
  let frame;
  const finish = () => {
    cancelAnimationFrame(frame);
    counters.forEach(counter => { counter.visual.textContent = counter.finalText; });
  };
  const observer = new IntersectionObserver(entries => {
    if (!entries.some(entry => entry.isIntersecting)) return;
    observer.disconnect(); // Animate only once per page load.
    if (reducedMotion.matches) return finish();
    const start = performance.now();
    const tick = now => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      counters.forEach(({ visual, target, suffix }) => {
        visual.textContent = `${Math.round(target * eased)}${suffix}`;
      });
      if (progress < 1) frame = requestAnimationFrame(tick);
      else finish();
    };
    tick(start);
  }, { threshold: 0.25 });
  observer.observe(section);
  reducedMotion.addEventListener('change', event => {
    if (event.matches) {
      observer.disconnect();
      finish();
    }
  });
})();
