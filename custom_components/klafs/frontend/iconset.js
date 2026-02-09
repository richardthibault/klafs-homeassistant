/**
 * Klafs Custom Icon Set - Inline SVG
 * Icons embedded directly in JS for maximum compatibility
 */

(() => {
  const tpl = document.createElement("template");
  tpl.innerHTML = `
    <ha-iconset-svg name="klafs" size="24">
      <svg viewBox="0 0 24 24">
        <defs>
          <!-- klafs:sauna -->
          <g id="sauna">
            <rect x="9" y="15" width="6" height="3" rx="0.5" fill="currentColor"/>
            <rect x="9.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="10.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="11.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="12.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="13.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <circle cx="10" cy="13.5" r="1.3" fill="currentColor"/>
            <circle cx="14" cy="13.5" r="1.3" fill="currentColor"/>
            <circle cx="12" cy="12" r="1.5" fill="currentColor"/>
            <rect x="4" y="18.5" width="16" height="1.5" rx="0.5" fill="currentColor"/>
            <circle cx="19" cy="11" r="1.2" fill="currentColor"/>
            <rect x="18.5" y="6" width="1" height="5" rx="0.3" fill="none" stroke="currentColor" stroke-width="0.8"/>
            <rect x="18.5" y="9.5" width="1" height="1.5" rx="0.3" fill="currentColor"/>
            <line x1="17.2" y1="10" x2="18.5" y2="10" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="8.5" x2="18.5" y2="8.5" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="7" x2="18.5" y2="7" stroke="currentColor" stroke-width="0.5"/>
          </g>

          <!-- klafs:sauna-heating -->
          <g id="sauna-heating">
            <rect x="9" y="15" width="6" height="3" rx="0.5" fill="currentColor"/>
            <rect x="9.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="10.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="11.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="12.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="13.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <circle cx="10" cy="13.5" r="1.3" fill="currentColor"/>
            <circle cx="14" cy="13.5" r="1.3" fill="currentColor"/>
            <circle cx="12" cy="12" r="1.5" fill="currentColor"/>
            <rect x="4" y="18.5" width="16" height="1.5" rx="0.5" fill="currentColor"/>
            <circle cx="19" cy="11" r="1.2" fill="currentColor"/>
            <rect x="18.5" y="6" width="1" height="5" rx="0.3" fill="none" stroke="currentColor" stroke-width="0.8"/>
            <rect x="18.5" y="8.5" width="1" height="2.5" rx="0.3" fill="currentColor"/>
            <line x1="17.2" y1="10" x2="18.5" y2="10" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="8.5" x2="18.5" y2="8.5" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="7" x2="18.5" y2="7" stroke="currentColor" stroke-width="0.5"/>
            <path d="M7,12 Q7,10.5 7.5,10.5 T8,12" stroke="currentColor" fill="none" stroke-width="0.7" stroke-linecap="round" opacity="0.7"/>
            <path d="M8.5,11 Q8.5,9.5 9,9.5 T9.5,11" stroke="currentColor" fill="none" stroke-width="0.7" stroke-linecap="round" opacity="0.7"/>
            <path d="M14.5,11 Q14.5,9.5 15,9.5 T15.5,11" stroke="currentColor" fill="none" stroke-width="0.7" stroke-linecap="round" opacity="0.7"/>
            <path d="M16,12 Q16,10.5 16.5,10.5 T17,12" stroke="currentColor" fill="none" stroke-width="0.7" stroke-linecap="round" opacity="0.7"/>
            <path d="M11,10 Q11,8.5 11.5,8.5 T12,10" stroke="currentColor" fill="none" stroke-width="0.7" stroke-linecap="round" opacity="0.7"/>
            <path d="M12.5,9.5 Q12.5,8 13,8 T13.5,9.5" stroke="currentColor" fill="none" stroke-width="0.7" stroke-linecap="round" opacity="0.7"/>
          </g>

          <!-- klafs:sauna-ready -->
          <g id="sauna-ready">
            <rect x="9" y="15" width="6" height="3" rx="0.5" fill="currentColor"/>
            <rect x="9.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="10.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="11.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="12.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <rect x="13.8" y="15.5" width="0.4" height="2" fill="#888"/>
            <circle cx="10" cy="13.5" r="1.3" fill="currentColor"/>
            <circle cx="14" cy="13.5" r="1.3" fill="currentColor"/>
            <circle cx="12" cy="12" r="1.5" fill="currentColor"/>
            <rect x="4" y="18.5" width="16" height="1.5" rx="0.5" fill="currentColor"/>
            <circle cx="19" cy="11" r="1.2" fill="currentColor"/>
            <rect x="18.5" y="6" width="1" height="5" rx="0.3" fill="none" stroke="currentColor" stroke-width="0.8"/>
            <rect x="18.5" y="6" width="1" height="5" rx="0.3" fill="currentColor"/>
            <line x1="17.2" y1="10" x2="18.5" y2="10" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="8.5" x2="18.5" y2="8.5" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="7" x2="18.5" y2="7" stroke="currentColor" stroke-width="0.5"/>
            <path d="M5,10 L6.5,11.5 L10,8" stroke="currentColor" stroke-width="1.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          </g>

          <!-- klafs:sauna-off -->
          <g id="sauna-off">
            <rect x="9" y="15" width="6" height="3" rx="0.5" fill="currentColor" opacity="0.3"/>
            <line x1="10" y1="15.5" x2="10" y2="17.5" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
            <line x1="11" y1="15.5" x2="11" y2="17.5" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
            <line x1="12" y1="15.5" x2="12" y2="17.5" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
            <line x1="13" y1="15.5" x2="13" y2="17.5" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
            <line x1="14" y1="15.5" x2="14" y2="17.5" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
            <circle cx="10" cy="13.5" r="1.3" fill="currentColor" opacity="0.3"/>
            <circle cx="14" cy="13.5" r="1.3" fill="currentColor" opacity="0.3"/>
            <circle cx="12" cy="12" r="1.5" fill="currentColor" opacity="0.3"/>
            <rect x="4" y="18.5" width="16" height="1.5" rx="0.5" fill="currentColor"/>
            <circle cx="19" cy="11" r="1.2" fill="currentColor"/>
            <rect x="18.5" y="6" width="1" height="5" rx="0.3" fill="none" stroke="currentColor" stroke-width="0.8"/>
            <line x1="17.2" y1="10" x2="18.5" y2="10" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="8.5" x2="18.5" y2="8.5" stroke="currentColor" stroke-width="0.5"/>
            <line x1="17.2" y1="7" x2="18.5" y2="7" stroke="currentColor" stroke-width="0.5"/>
          </g>
        </defs>
      </svg>
    </ha-iconset-svg>
  `;

  document.body.appendChild(tpl.content);
  // eslint-disable-next-line no-console
  console.info("[Klafs Icons] Inline iconset loaded - klafs:sauna, klafs:sauna-heating, klafs:sauna-ready, klafs:sauna-off");
})();
