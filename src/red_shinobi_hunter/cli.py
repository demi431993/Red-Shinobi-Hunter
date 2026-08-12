import argparse
import json

from .config import ScanConfig
from .scanner import probe, result_dict


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="red-shinobi-hunter", description="Authorized defensive target probe")
    parser.add_argument("targets", nargs="+", help="URLs/hosts you are authorized to assess")
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--rate", type=float, default=2.0, help="maximum probe rate")
    parser.add_argument("--max-targets", type=int, default=64)
    parser.add_argument("--stealth", action="store_true", help="enable assessment pacing jitter")
    parser.add_argument("--jitter-min", type=float, default=0.0)
    parser.add_argument("--jitter-max", type=float, default=0.0)
    parser.add_argument("--json", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config = ScanConfig(
        timeout=args.timeout,
        max_targets=args.max_targets,
        requests_per_second=args.rate,
        stealth=args.stealth,
        jitter_min=args.jitter_min,
        jitter_max=args.jitter_max,
    )
    results = [result_dict(probe(target, config)) for target in args.targets[:config.max_targets]]
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for item in results:
            print(f"{item['target']} status={item['status']} server={item['server']} type={item['content_type']} error={item['error']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
