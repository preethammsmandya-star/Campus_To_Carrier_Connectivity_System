import os
import re

replacements = {
    r'\btext-white\b': 'text-slate-800',
    r'\btext-slate-400\b': 'text-slate-500',
    r'\bbg-slate-800/50\b': 'bg-white',
    r'\bbg-slate-800/30\b': 'bg-white/60',
    r'\bbg-slate-700/50\b': 'bg-slate-50',
    r'\bborder-slate-700/50\b': 'border-slate-200',
    r'\bbg-slate-700\b': 'bg-slate-200',
    r'\btext-slate-300\b': 'text-slate-600',
    r'\bbg-slate-800\b': 'bg-white',
    r'\bbg-slate-900\b': 'bg-slate-50',
}

def process():
    for root, _, files in os.walk('frontend/src/pages'):
        for file in files:
            if file.endswith('.jsx'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Protect hero banners
                # Find <div className="relative rounded-2xl... and its inner content up to </div>\s*</div>
                hero_pattern = re.compile(r'(<div className="relative rounded-2xl overflow-hidden mb-8".*?<!-- HERO END -->|relative z-10 p-8 md:p-12 h-full.*?</p>)', re.DOTALL)
                
                def protect(match):
                    return match.group(0).replace('text-white', 'TEXT_WHITE_PROTECTED').replace('text-slate-400', 'TEXT_SLATE_400_PROTECTED')
                
                content = hero_pattern.sub(protect, content)
                
                # Replace classes
                for old, new in replacements.items():
                    content = re.sub(old, new, content)
                    
                # Restore
                content = content.replace('TEXT_WHITE_PROTECTED', 'text-white').replace('TEXT_SLATE_400_PROTECTED', 'text-slate-400')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    process()
