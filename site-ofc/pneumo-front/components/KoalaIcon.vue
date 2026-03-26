<template>
  <div class="flex-shrink-0 group">
    <div class="w-10 h-10 md:w-12 md:h-12 flex items-center justify-center bg-gradient-to-br from-indigo-500 via-indigo-600 to-violet-700 rounded-[1.15rem] shadow-[0_8px_20px_-6px_rgba(99,102,241,0.5)] text-white mt-1 border border-white/20 dark:border-white/10 transition-all duration-500 relative overflow-hidden ring-2 ring-transparent group-hover:ring-indigo-300/50">
      
      <div class="absolute top-0 inset-x-0 h-1/2 bg-gradient-to-b from-white/30 to-transparent"></div>
      <div class="absolute bottom-0 inset-x-0 h-1/3 bg-gradient-to-t from-black/20 to-transparent"></div>

      <svg
        width="48"
        height="48"
        viewBox="0 0 48 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        class="w-8 h-8 md:w-10 md:h-10 transition-all duration-500 relative z-10 drop-shadow-[0_4px_4px_rgba(0,0,0,0.15)] group-hover:scale-105"
      >
        <defs>
          <linearGradient id="faceGrad" x1="24" y1="5" x2="24" y2="45" gradientUnits="userSpaceOnUse">
            <stop stop-color="#F8FAFC" />
            <stop offset="1" stop-color="#CBD5E1" />
          </linearGradient>
          <linearGradient id="earGrad" x1="0" y1="10" x2="0" y2="26" gradientUnits="userSpaceOnUse">
            <stop stop-color="#FFFFFF" />
            <stop offset="1" stop-color="#E2E8F0" />
          </linearGradient>
          <linearGradient id="noseGrad" x1="24" y1="23" x2="24" y2="38" gradientUnits="userSpaceOnUse">
            <stop stop-color="#334155" />
            <stop offset="1" stop-color="#0F172A" />
          </linearGradient>
          <linearGradient id="glassGrad" x1="10" y1="20" x2="38" y2="27" gradientUnits="userSpaceOnUse">
            <stop stop-color="#38BDF8" stop-opacity="0.4" />
            <stop offset="0.5" stop-color="#818CF8" stop-opacity="0.1" />
            <stop offset="1" stop-color="#38BDF8" stop-opacity="0.4" />
          </linearGradient>
        </defs>

        <circle cx="9" cy="18" r="8" fill="url(#earGrad)" />
        <circle cx="9" cy="18" r="4.5" fill="#94A3B8" />
        <circle cx="39" cy="18" r="8" fill="url(#earGrad)" />
        <circle cx="39" cy="18" r="4.5" fill="#94A3B8" />

        <circle cx="24" cy="25" r="20" fill="url(#faceGrad)" />
        
        <ellipse cx="24" cy="31" rx="5.5" ry="8" fill="url(#noseGrad)" />
        <ellipse cx="24" cy="26" rx="2.5" ry="1.5" fill="#FFFFFF" opacity="0.6" />

        <g v-if="expression === 'neutral'" class="transition-opacity duration-300">
          <circle cx="15" cy="23" r="2.5" fill="#0F172A" />
          <circle cx="33" cy="23" r="2.5" fill="#0F172A" />
          <circle cx="15.5" cy="22" r="1" fill="#FFFFFF" /> 
          <circle cx="33.5" cy="22" r="1" fill="#FFFFFF" />
          <path d="M21,41 Q24,43 27,41" stroke="#0F172A" stroke-width="1.8" stroke-linecap="round" fill="none" />
        </g>

        <g v-else-if="expression === 'happy'" class="transition-opacity duration-300">
          <ellipse cx="12" cy="28" rx="3.5" ry="2" fill="#F472B6" opacity="0.5" filter="blur(1px)" />
          <ellipse cx="36" cy="28" rx="3.5" ry="2" fill="#F472B6" opacity="0.5" filter="blur(1px)" />
          <path d="M12,24 Q15,20 18,24" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none" />
          <path d="M30,24 Q33,20 36,24" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none" />
          <path d="M20,40 Q24,46 28,40 Z" fill="#0F172A" />
          <path d="M22,41.5 Q24,44.5 26,41.5 Z" fill="#FB7185" /> 
        </g>

        <g v-else-if="expression === 'analytical'" class="transition-opacity duration-300">
          <rect x="9" y="19" width="12" height="8" rx="3" stroke="#60A5FA" stroke-width="1.5" fill="url(#glassGrad)" />
          <rect x="27" y="19" width="12" height="8" rx="3" stroke="#60A5FA" stroke-width="1.5" fill="url(#glassGrad)" />
          <line x1="21" y1="23" x2="27" y2="23" stroke="#60A5FA" stroke-width="1.5" />
          <line x1="11" y1="25" x2="15" y2="21" stroke="#FFFFFF" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
          <line x1="29" y1="25" x2="33" y2="21" stroke="#FFFFFF" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
          <circle cx="15" cy="23" r="2" fill="#0F172A" />
          <circle cx="33" cy="23" r="2" fill="#0F172A" />
          <path d="M11,18 Q14,16 17,18" stroke="#0F172A" stroke-width="1.5" stroke-linecap="round" fill="none" />
          <path d="M29,19 Q32,18 35,19" stroke="#0F172A" stroke-width="1.5" stroke-linecap="round" fill="none" />
          <line x1="22" y1="41" x2="26" y2="41" stroke="#0F172A" stroke-width="1.8" stroke-linecap="round" />
        </g>

        <g v-else-if="expression === 'confused'" class="transition-opacity duration-300">
          <path d="M13,21 L17,25 M17,21 L13,25" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" />
          <path d="M31,21 L35,25 M35,21 L31,25" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" />
          <path d="M38,14 Q41,18 38,21 Q35,18 38,14 Z" fill="#38BDF8" opacity="0.9" />
          <circle cx="39" cy="18" r="1" fill="#FFFFFF" opacity="0.6" />
          <path d="M20,41 Q22,39 24,41 T28,41" stroke="#0F172A" stroke-width="1.8" stroke-linecap="round" fill="none" />
        </g>

        <g v-else-if="expression === 'surprised'" class="transition-opacity duration-300">
          <circle cx="15" cy="22" r="4.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="1.5" />
          <circle cx="33" cy="22" r="4.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="1.5" />
          <circle cx="15" cy="22" r="1.8" fill="#0F172A" />
          <circle cx="33" cy="22" r="1.8" fill="#0F172A" />
          <path d="M12,15 Q15,13 18,15" stroke="#0F172A" stroke-width="1.5" stroke-linecap="round" fill="none" />
          <path d="M30,15 Q33,13 36,15" stroke="#0F172A" stroke-width="1.5" stroke-linecap="round" fill="none" />
          <circle cx="24" cy="42" r="3" fill="#0F172A" />
        </g>

        <g v-else>
          <circle cx="15" cy="23" r="2.5" fill="#0F172A" />
          <circle cx="33" cy="23" r="2.5" fill="#0F172A" />
          <circle cx="15.5" cy="22" r="1" fill="#FFFFFF" /> 
          <circle cx="33.5" cy="22" r="1" fill="#FFFFFF" />
        </g>

      </svg>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  expression?: 'neutral' | 'happy' | 'analytical' | 'confused' | 'surprised'
}>();
</script>