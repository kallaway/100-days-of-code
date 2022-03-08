import { paginate, resolver } from "blitz"
import db, { Prisma } from "db"

interface GetChoicesInput
  extends Pick<Prisma.ChoiceFindManyArgs, "where" | "orderBy" | "skip" | "take"> {}

export default resolver.pipe(
  resolver.authorize(),
  async ({ where, orderBy, skip = 0, take = 100 }: GetChoicesInput) => {
    // TODO: in multi-tenant app, you must add validation to ensure correct tenant
    const {
      items: choices,
      hasMore,
      nextPage,
      count,
    } = await paginate({
      skip,
      take,
      count: () => db.choice.count({ where }),
      query: (paginateArgs) => db.choice.findMany({ ...paginateArgs, where, orderBy }),
    })

    return {
      choices,
      nextPage,
      hasMore,
      count,
    }
  }
)
