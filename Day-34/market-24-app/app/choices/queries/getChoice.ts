import { resolver, NotFoundError } from "blitz"
import db from "db"
import { z } from "zod"

const GetChoice = z.object({
  // This accepts type of undefined, but is required at runtime
  id: z.number().optional().refine(Boolean, "Required"),
})

export default resolver.pipe(resolver.zod(GetChoice), resolver.authorize(), async ({ id }) => {
  // TODO: in multi-tenant app, you must add validation to ensure correct tenant
  const choice = await db.choice.findFirst({ where: { id } })

  if (!choice) throw new NotFoundError()

  return choice
})
