/* ── Connectly App JS ──────────────────────────────────────── */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Mobile nav toggle ────────────────────────────────── */
  const navToggle = document.getElementById('navToggle');
  const navLinks  = document.getElementById('navLinks');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      const open = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open);
      navToggle.innerHTML = open
        ? `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>`
        : `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/></svg>`;
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', false);
      }
    });
  }

  /* ── Auto-dismiss flash messages ─────────────────────── */
  document.querySelectorAll('.message').forEach((msg, i) => {
    setTimeout(() => {
      msg.style.transition = 'opacity 0.4s, transform 0.4s';
      msg.style.opacity = '0';
      msg.style.transform = 'translateY(-6px)';
      setTimeout(() => msg.remove(), 400);
    }, 4000 + i * 600);
  });

  /* ── Auto-resize comment textareas ───────────────────── */
  document.querySelectorAll('.comment-textarea').forEach(ta => {
    const resize = () => {
      ta.style.height = 'auto';
      ta.style.height = Math.min(ta.scrollHeight, 100) + 'px';
    };
    ta.addEventListener('input', resize);
    // Submit on Enter (not Shift+Enter)
    ta.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        ta.closest('form').submit();
      }
    });
  });

  /* ── Like button pulse animation ─────────────────────── */
  document.querySelectorAll('.like-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      this.style.transform = 'scale(1.4)';
      setTimeout(() => { this.style.transform = ''; }, 300);
    });
  });

  /* ── Search live feedback ─────────────────────────────── */
  const searchInput = document.querySelector('.search-main-input');
  if (searchInput) {
    searchInput.focus();
  }

  /* ── Profile avatar initials fallback ────────────────── */
  document.querySelectorAll('[data-initials]').forEach(el => {
    const img = el.querySelector('img');
    if (img) {
      img.addEventListener('error', () => {
        img.remove();
        el.textContent = el.dataset.initials;
      });
    }
  });
});
